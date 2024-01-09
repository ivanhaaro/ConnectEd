import json
import requests
from models.data_model import DataModel
from extractors.validations import Validations



class CVExtractor:
    def extract_data(self):
        # url de la api de murcia
        url = "http://127.0.0.1:8083/"
        try:
            response = requests.get(url)
            response.raise_for_status()

            cvData = response.json()
            print("Respuesta de la API:")
            print(cvData)
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")

        data = []
        errors = []
        validations = Validations()

        with cvData as json_data:
            data_list = json.load(json_data)

            for item in data_list:
                # Create DataModel objects for each JSON item

                # Detect name errors
                dencen = item['DENOMINACION']
                if not validations.isValidString(dencen):
                    errors.append('ERROR: COMUNIDAD VALENCIANA, El nombre del centro "' + dencen + '" es inválido.')
                    continue

                # Transform titularidad into tipo
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

                # Detect direccion errors
                domcen = item['domcen']
                if not validations.isValidString(domcen):
                    errors.append('WARNING: COMUNIDAD VALENCIANA, La dirección "' + domcen + '" del centro: ' + domcen + ' es inválida.')

                direc = None
                if 'TIPO_VIA' in item and 'DIRECCION' in item and 'NUMERO' in item:
                    direc = f"{item['TIPO_VIA']} {item['DIRECCION']} {item['NUMERO']}"
                    if not validations.isValidString(direc):
                        errors.append('ERROR: COMUNIDAD VALENCIANA, La dirección "' + direc + '" del centro: ' + dencen + ' es inválida.')
                        continue
                else:
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La dirección no existe.')
                    continue

                # Latitude and Longitude error detection

                if 'LONGITUD' in item:
                        lon = item['LONGITUD']
                        if not validations.isValidString(str(lon)):
                            errors.append('ERROR: COMUNIDAD VALENCIANA, La longitud "' + lon + '" del centro: ' + dencen + ' es inválida.') 
                            continue
                else:
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La longitud del centro: ' + dencen + ' no se ha podido obtener')
                    continue  
                if 'LATITTUD' in item:
                        lat = item['LATITUD']
                        if not validations.isValidString(str(lat)):
                            errors.append('ERROR: COMUNIDAD VALENCIANA, La latitud "' + lat + '" del centro: ' + dencen + ' es inválida.')
                            continue
                else:
                    errors.append('ERROR: COMUNIDAD VALENCIANA, La latitud del centro: ' + dencen + ' no se ha podido obtener.')
                    continue

                #Phone number error detection
                tel = ''
                if 'TELEFONO' in item:
                    tel = item['TELEFONO'].strip()  
                    if not validations.isValidPhoneNum(tel):  
                        errors.append('ERROR: COMUNIDAD VALENCIANA, El número de teléfono "' + tel + '" del centro: ' + dencen + ' es inválido.')
                        continue   

                #Postal code error detection
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
                data.append(data_model)

        return data, errors
    
