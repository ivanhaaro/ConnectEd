import json
import re
import requests
from models.data_model import DataModel
from extractors.validations import Validations



class MURExtractor:
    def extract_data(self):
        # url de la api de murcia
        url = "http://127.0.0.1:8082/"
        try:
            response = requests.get(url)
            response.raise_for_status()

            catData = response.json()
            print("Respuesta de la API:")
            print(catData)
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")

        data = []
        errors = []
        validations = Validations()

        with catData as json_data:
            data_list = json.load(json_data)

            for item in data_list:
                

                # Detect name errors
                if 'denominaci_completa' in item:
                    nombre = item['denominaci_completa']
                    if not validations.isValidString(nombre):
                        errors.append('ERROR: CATALUÑA, El nombre del centro "' + nombre + '" es inválido.')
                        continue
                else:
                    errors.append('ERROR: CATALUÑA, No esta especificado el nombre del centro')
                    continue
                # Detect cod post errors
                cod = ''
                if 'codi_postal' in item:
                    cod = item['codi_postal']
                    if not validations.isValidPostalCode(cod):
                        errors.append('ERROR: CATALUÑA, El código postal "' + cod + '" del centro: ' + nombre + ' es inválido.')
                        continue
                else:
                    errors.append('ERROR: CATALUÑA, El código postal del centro: ' + nombre + ' no está')
                    continue
            
                # Crear un objeto DataModel a partir de los datos de la fila
                if 'codi_postal' in item and 'nom_municipi' in item :
                    codP = item['codi_postal']
                    codP = codP[:2]
                    if codP == '08':
                        provincia = 'Barcelona'
                    elif codP == '17':
                        provincia = 'Girona'
                    elif codP == '25':
                        provincia = 'Lleida'
                    elif codP == '43':
                        provincia = 'Tarragona'
                    else:
                        errors.append('ERROR: CATALUÑA, La provincia especificada no es válida')
                        continue
                
                    localidad = {'codigo': '', 'nombre': item['nom_municipi']}
                    provincia = {
                        'codigo': codP, 'nombre': provincia}
                else:
                    errors.append('ERROR: CATALUÑA, El nombre municipio no esta especificado')
                    continue
            
                if 'nom_naturalesa' in item:
                    tipo = item['nom_naturalesa']
                    if tipo == 'Privat':
                        tipo = 'Privado'
                    elif tipo == 'Públic':
                        tipo = 'Publico'
                    else:
                        errors.append('ERROR: CATALUÑA, El tipo especificado no es correcto')
                        continue

            

                # Detect LONG AND LAT errors
                if 'coordenades_geo_x' in item and 'coordenades_geo_y' in item :
                        lon = item['coordenades_geo_x']
                        lat = item['coordenades_geo_y']
                        if lon == None or lat == None:
                            errors.append('ERROR: CATALUÑA, La latitud o la longitud no está correctamente espeificada')
                            continue  
                else:
                        if 'georefer_ncia' in item:
                            cadena = re.search(r'\((.*?)\)', item['georefer_ncia'])
                            if cadena:
                                numeros = cadena.group(1)
                                numeros = numeros.split()
                                lat = numeros[1]
                                lon = numeros[0]
                            else:
                                errors.append('ERROR: CATALUÑA, La latitud o la longitud no está correctamente espeificada')
                                continue
                        else: 
                            errors.append('ERROR: CATALUÑA, La latitud o la longitud no está correctamente espeificada')
                            continue
            
                # Detect address errors
                direccion = None
                if 'adre_a' in item:
                    direccion = item['adre_a']
                    if not validations.isValidString(direccion):
                        errors.append('WARNING: CATALUÑA, La dirección "' + direccion + '" del centro: ' + nombre + ' es inválida.')

            


                data_model = DataModel(
                    nombre= nombre,
                    tipo= tipo,
                    codigo_postal=cod,
                    direccion= direccion,
                    longitud=lon,
                    latitud=lat,
                    telefono= '',
                    descripcion= '',
                    localidad=localidad,
                    provincia=provincia,

                )

                data.append(data_model)

        return data, errors
    
