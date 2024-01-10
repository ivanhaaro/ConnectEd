import json
import requests
from models.data_model import DataModel
from extractors.validations import Validations

class MURExtractor:
    def extract_data(self):
        # URL de la API de Murcia
        url = "http://127.0.0.1:8081/"
        
        try:
            # Realiza una solicitud GET a la API
            response = requests.get(url)
            response.raise_for_status()  # Genera una excepción si hay un error HTTP
            
            # Convierte la respuesta JSON en un diccionario
            murciaData = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")

        data = []  # Lista para almacenar los objetos DataModel
        errors = []  # Lista para almacenar mensajes de error
        geos = set() 
        validations = Validations()  # Instancia de la clase Validations para validar datos

        # Itera sobre los datos obtenidos de la API
        for item in murciaData:
            # Validaciones y procesamiento de cada elemento en los datos

            # Detecta errores en el nombre del centro
            dencen = item['dencen']
            if not validations.isValidString(dencen):
                errors.append('ERROR: MURCIA, El nombre del centro "' + dencen + '" es inválido.')
                continue

            # Transforma la titularidad en tipo
            titularidad = item['titularidad']
            if titularidad == 'P':
                titularidad = 'Publico'
            elif titularidad == 'N':
                titularidad = 'Privado'
            elif titularidad == 'C':
                titularidad = 'Concertado'
            else:
                errors.append('ERROR: MURCIA, El tipo "' + titularidad + '" del centro: ' + dencen + ' es inválido')
                continue

            # Detecta errores en la dirección del centro
            domcen = item['domcen']
            if not validations.isValidString(domcen):
                errors.append('ERROR: MURCIA, La dirección "' + domcen + '" del centro: ' + dencen + ' es inválida.')
                continue

            # Detección de errores en latitud y longitud
            if 'geo-referencia' in item:
                referencia = item['geo-referencia']
                
                if 'lon' in referencia:
                    lon = item['geo-referencia']['lon']
                    if not validations.isValidString(str(lon)):
                        errors.append('ERROR: MURCIA, La longitud "' + lon + '" del centro: ' + dencen + ' es inválida.') 
                        continue
                else:
                    errors.append('ERROR: MURCIA, La longitud del centro: ' + dencen + ' es no está especificada') 
                    continue

                if 'lat' in referencia:
                    lat = item['geo-referencia']['lat']
                    if not validations.isValidString(str(lat)):
                        errors.append('ERROR: MURCIA, La latitud "' + lat + '" del centro: ' + dencen + ' es inválida.')
                        continue
                else:
                    errors.append('ERROR: MURCIA, La latitud del centro: ' + dencen + ' es no está especificada') 
                    continue
            else:
                errors.append('ERROR: MURCIA, La latitud y longitud del centro: ' + dencen + ' son inválidas.')
                continue

            # Detección de errores en el número de teléfono
            tel = ''
            if 'telcen' in item:
                tel = item['telcen'].strip()  
                if not validations.isValidString(tel):
                    errors.append('WARNING: MURCIA, El número de teléfono "' + tel + '" del centro: ' + dencen + ' está vacío.')
                    tel = ''
                elif not validations.isValidPhoneNum(tel):  
                    errors.append('ERROR: MURCIA, El número de teléfono "' + tel + '" del centro: ' + dencen + ' es inválido.')
                    continue   

            # Detección de errores en el código postal
            if 'cpcen' in item:
                cpcen = item['cpcen']
                if not validations.isValidPostalCode(cpcen):
                    errors.append('ERROR: MURCIA, El código postal "' + cpcen + '" del centro: ' + dencen + ' es inválido.')
                    continue

            # Detección de errores en la descripción
            descp = ''
            if 'presentacionCorta' in item:
                descp = item['presentacionCorta']

            # Detección de errores en la localidad
            if 'loccen' in item:
                loccen = item['loccen']
                if not validations.isValidString(loccen):
                    errors.append('ERROR: MURCIA, La localidad "' + loccen + '" del centro: ' + dencen + ' es inválida.')
                    continue
                else:
                    localidad = {'codigo': item['cpcen'], 'nombre': loccen}

            provincia = {'codigo': '30', 'nombre': 'Murcia'}   

            # Crea objetos DataModel para cada elemento JSON
            data_model = DataModel(
                nombre=dencen,
                tipo=titularidad,
                direccion=domcen,
                codigo_postal=cpcen,
                longitud=lon,
                latitud=lat,
                telefono=tel,
                descripcion=descp,
                localidad=localidad,
                provincia=provincia
            )

            hash_code = lat+lon

            if hash_code in geos:
                errors.append('ERROR: MURCIA, El centro ' + dencen + ' ya se encuentra en la base de datos.')
                continue
            else:
                geos.add(hash_code)

            data.append(data_model)  # Agrega el objeto DataModel a la lista
        errors.append('Número de centros cargados en REGIÓN DE MURCIA: ' + str(len(geos)))
        return data, errors  # Devuelve la lista de objetos DataModel y la lista de errores
