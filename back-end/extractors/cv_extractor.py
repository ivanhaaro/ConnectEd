import json
import requests
from models.data_model import DataModel
from extractors.validations import Validations

class CVExtractor:
    def extract_data(self):
        # URL de la API de la Comunidad Valenciana
        url = "http://127.0.0.1:8083/"
        
        try:
            # Realiza una solicitud GET a la API
            response = requests.get(url)
            response.raise_for_status()  # Genera una excepción si hay un error HTTP
            
            # Convierte la respuesta JSON en un diccionario
            cvData = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")

        data = []  # Lista para almacenar los objetos DataModel
        errors = []  # Lista para almacenar mensajes de error
        geos = set()
        validations = Validations()  # Instancia de la clase Validations para validar datos

        # Itera sobre los datos obtenidos de la API
        for item in cvData:
            # Validaciones y procesamiento de cada elemento en los datos

            # Detecta errores en el nombre del centro
            dencen = item['DENOMINACION']
            if not validations.isValidString(dencen):
                errors.append('ERROR: COMUNIDAD VALENCIANA, El nombre del centro "' + dencen + '" es inválido.')
                continue

            # Transforma la titularidad en tipo
            titularidad = item['REGIMEN']
            if titularidad == 'PÚB.':
                titularidad = 'Publico'
            elif titularidad == 'PRIV.':
                titularidad = 'Privado'
            elif titularidad == 'PRIV. CONC.':
                titularidad = 'Concertado'
            elif titularidad == 'OTROS':
                titularidad = 'Otros'
            else:
                errors.append(f'ERROR: COMUNIDAD VALENCIANA, El tipo {titularidad} es inválido')
                continue

            # Detecta errores en la dirección del centro
            direc = None
            if 'TIPO_VIA' in item and 'DIRECCION' in item and 'NUMERO' in item:
                direc = f"{item['TIPO_VIA']} {item['DIRECCION']} {item['NUMERO']}"
                if not validations.isValidString(direc):
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La dirección "' + direc + '" del centro: ' + dencen + ' es inválida.')
                    continue
            else:
                errors.append('ERROR: COMUNIDAD VALENCIANA, La dirección no existe.')
                continue

            # Detección de errores en latitud y longitud
            if 'LONGITUD' in item:
                lon = item['LONGITUD']
                if not validations.isValidString(lon):
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La longitud "' + lon + '" del centro: ' + dencen + ' es inválida.') 
                    continue
            else:
                errors.append('ERROR: COMUNIDAD VALENCIANA, La longitud del centro: ' + dencen + ' no se ha podido obtener')
                continue  
            
            if 'LATITUD' in item:
                lat = item['LATITUD']
                if not validations.isValidString(lat):
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La latitud "' + lat + '" del centro: ' + dencen + ' es inválida.')
                    continue
            else:
                errors.append('ERROR: COMUNIDAD VALENCIANA, La latitud del centro: ' + dencen + ' no se ha podido obtener.')
                continue

            # Detección de errores en el número de teléfono
            tel = ''
            if 'TELEFONO' in item:
                tel = item['TELEFONO'].strip()  
                if not validations.isValidString(tel):
                    errors.append('WARNING: COMUNIDAD VALENCIANA, El número de teléfono "' + tel + '" del centro: ' + dencen + ' está vacío.')
                    tel = ''
                elif not validations.isValidPhoneNum(tel):  
                    errors.append('ERROR: COMUNIDAD VALENCIANA, El número de teléfono "' + tel + '" del centro: ' + dencen + ' es inválido.')
                    continue   

            # Detección de errores en el código postal
            if 'CODIGO_POSTAL' in item:
                cpcen = item['CODIGO_POSTAL']
                if validations.isAlicante(cpcen):
                    cpcen = '0' + cpcen
                    errors.append('WARNING: COMUNIDAD VALENCIANA, El código postal "' + cpcen + '"ha sido completado debido a su incorrecto formato')
                elif not validations.isValidPostalCode(cpcen):
                    errors.append('ERROR: COMUNIDAD VALENCIANA, El código postal "' + cpcen + '" del centro: ' + dencen + ' es inválido.')
                    continue
                if 'LOCALIDAD' in item:
                    localidad = {'codigo': cpcen, 'nombre': item['LOCALIDAD']}
                if 'PROVINCIA' in item:
                    provincia = {'codigo': cpcen[:2], 'nombre': item['PROVINCIA']}
            else:
                errors.append('ERROR: COMUNIDAD VALENCIANA, El código postal no está especificado')
                continue

            data_model = DataModel(
                    nombre=dencen,
                    tipo=titularidad,
                    direccion=direc,
                    codigo_postal=cpcen,
                    longitud=lon,
                    latitud=lat,
                    telefono=tel,
                    descripcion=item['DENOMINACION_ESPECIFICA'],
                    localidad=localidad,
                    provincia=provincia
            )

            hash_code = lat+lon

            if hash_code in geos:
                errors.append('ERROR: COMUNIDAD VALENCIANA, El centro ' + dencen + ' ya se encuentra en la base de datos.')
                continue
            else:
                geos.add(hash_code)

            
            data.append(data_model)  # Agrega el objeto DataModel a la lista

        return data, errors  # Devuelve la lista de objetos DataModel y la lista de errores
