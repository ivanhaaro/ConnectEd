import json
from models.data_model import DataModel
from extractors.validations import Validations

class JSONExtractor:
    def extract_data(self, file_path):

        data = []
        errors = []
        validations = Validations()

        with open(file_path, 'r', encoding='utf-8') as json_file:
            data_list = json.load(json_file)

            for item in data_list:
                # Create DataModel objects for each JSON item

                # Detect name errors
                dencen = item['dencen']
                if not validations.isValidString(dencen):
                    errors.append('ERROR: El nombre del centro "' + dencen + '" es inválido.')
                    continue

                # Transform titularidad into tipo
                titularidad = item['titularidad']
                if titularidad == 'P':
                    titularidad = 'Publico'
                elif titularidad == 'N':
                    titularidad = 'Privado'
                elif titularidad == 'C':
                    titularidad = 'Concertado'
                else:
                    errors.append('ERROR: El tipo "' + titularidad + '" del centro: ' + domcen + ' es inválido')
                    continue

                # Detect direccion errors
                domcen = item['domcen']
                if not validations.isValidString(domcen):
                    errors.append('WARNING: La dirección "' + domcen + '" del centro: ' + domcen + ' es inválida.')

                # Latitude and Longitude error detection
                if 'geo-referencia' in item:
                    referencia = item['geo-referencia']

                    if 'lon' in referencia:
                        lon = item['geo-referencia']['lon']
                        if not validations.isValidString(str(lon)):
                            errors.append('ERROR: La longitud "' + lon + '" del centro: ' + dencen + ' es inválida.') 
                            continue
                    
                    if 'lat' in referencia:
                        lat = item['geo-referencia']['lat']
                        if not validations.isValidString(str(lat)):
                            errors.append('ERROR: La latitud "' + lat + '" del centro: ' + dencen + ' es inválida.')
                            continue
                else:
                    errors.append('ERROR: La latitud y longitud del centro: ' + dencen + ' son inválidas.')
                    continue

                #Phone number error detection
                tel = ''
                if 'telcen' in item:
                    tel = item['telcen'].strip()  
                    if not validations.isValidPhoneNum(tel):  
                        errors.append('ERROR: El número de teléfono "' + tel + '" del centro: ' + dencen + ' es inválido.')
                        continue   

                #Postal code error detection
                if 'cpcen' in item:
                    cpcen = item['cpcen']
                    if not validations.isValidPostalCode(cpcen):
                        errors.append('ERROR: El código postal "' + cpcen + '" del centro: ' + dencen + ' es inválido.')
                        continue

                #Description error detection
                descp = ''
                if 'presentacionCorta' in item:
                    descp = item['presentacionCorta']
                    # if not validations.isValidString(descp):
                    #     errors.append('La descripción "' + descp + '" del centro: ' + dencen + ' es inválida.')

                if 'loccen' in item:
                    loccen = item['loccen']
                    if not validations.isValidString(loccen):
                        errors.append('ERROR: La localidad "' + loccen + '" del centro: ' + dencen + ' es inválida.')
                        continue
                    else:
                        localidad = {'codigo': item['cpcen'], 'nombre': loccen}

                provincia = {'codigo': '30', 'nombre': 'Murcia'}   

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

                data.append(data_model)

        return data, errors
    
