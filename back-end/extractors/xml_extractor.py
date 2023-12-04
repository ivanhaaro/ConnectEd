import xml.etree.ElementTree as ET
from models.data_model import DataModel
from extractors.validations import Validations
import re

class XMLExtractor:
    def extract_data(self, file_path):
        data = []
        errors = []
        validations = Validations()
        tree = ET.parse(file_path)
        root = tree.getroot()

        for row in root.findall('.//row'):
            # Crear un diccionario para almacenar datos de cada fila
            row_data = {}

            # Iterar sobre los elementos hijos de la fila
            for element in row:
                # Utilizar el nombre del elemento como clave y su texto como valor
                row_data[element.tag] = element.text

            # Crear un objeto DataModel a partir de los datos de la fila
            if 'codi_postal' in row_data and 'nom_municipi' in row_data :
                codP = row_data.get('codi_postal')
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
                     errors.append('La provincia especificada no es válida')
                     continue
                
                localidad = {'codigo': '', 'nombre': row_data.get('nom_municipi')}
                provincia = {
                    'codigo': codP, 'nombre': provincia}
            else:
                 errors.append('El codigo postal o nombre municipio no esta especificado')
                 continue
            
            if 'nom_naturalesa' in row_data:
                tipo = row_data.get('nom_naturalesa')
                if tipo == 'Privat':
                    tipo = 'Privado'
                elif tipo == 'Públic':
                    tipo = 'Público'
                else:
                     errors.append('El tipo especificado no es correcto')
                     continue

            # Detect name errors
            if 'denominaci_completa' in row_data:
                nombre = row_data.get('denominaci_completa')
                if not validations.isValidString(nombre):
                    errors.append('El nombre del centro "' + nombre + '" es inválido.')
                    continue
            else:
                 errors.append('No esta especificado el nombre del centro')
                 continue

            # Detect LONG AND LAT errors
            if 'coordenades_geo_x' in row_data and 'coordenades_geo_y' in row_data :
                    lon = row_data.get('coordenades_geo_x')
                    lat = row_data.get('coordenades_geo_y')
            else:
                    if 'georefer_ncia' in row_data:
                         cadena = re.search(r'\((.*?)\)', row_data.get('georefer_ncia'))
                         if cadena:
                              numeros = cadena.group(1)
                              numeros = numeros.split()
                              lat = numeros[1]
                              lon = numeros[0]
                         else:
                              errors.append('La latitud o la longitud no está correctamente espeificada')
                              continue
                    else: 
                        errors.append('La latitud o la longitud no está correctamente espeificada')
                        continue
            
            # Detect address errors
            direccion = None
            if 'adre_a' in row_data:
                direccion = row_data.get('adre_a')
                if not validations.isValidString(direccion):
                    errors.append('La dirección "' + direccion + '" del centro: ' + nombre + ' es inválida.')

            # Detect cod post errors
            cod = ''
            if 'codi_postal' in row_data:
                cod = row_data.get('codi_postal')
                if not validations.isValidPostalCode(cod):
                    errors.append('El código postal "' + cod + '" del centro: ' + nombre + ' es inválido.')
                    continue
            else:
                 continue


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

            # Agregar el objeto DataModel a la lista de datos
            data.append(data_model)

        return data, errors

