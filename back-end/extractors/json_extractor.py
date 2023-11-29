import json
from models.data_model import DataModel
from extractors.validations import Validations

class JSONExtractor:
    def extract_data(self, file_path):

        data = []
        errors = []
        validations = Validations()

        with open(file_path, 'r') as json_file:
            data_list = json.load(json_file)

            for item in data_list:
                # Create DataModel objects for each JSON item

                # Detect name errors
                dencen = item['dencen']
                if not validations.isValidString(dencen):
                    errors.append('El nombre del centro (' + domcen + ') es inválido.')

                # Transform titularidad into tipo
                titularidad = item['titularidad']
                if titularidad == 'P':
                    titularidad = 'Público'
                elif titularidad == 'N':
                    titularidad = 'Privado'
                elif titularidad == 'C':
                    titularidad = 'Concertado'
                else:
                    titularidad = 'Otro'

                # Detect direccion errors
                domcen = item['domcen']
                if not validations.isValidString(domcen):
                    errors.append('La dirección del centro ' + domcen + ' es inválida.')

                # Latitude and Longitude error detection
                if 'geo-referencia' in item:
                    lon = item['geo-referencia']['lon']
                    lat = item['geo-referencia']['lat']
                else:
                    continue

                #Phone number error detection
                tel = None
                if 'telcen' in item:
                    tel = item['telcen']  
                    if not validations.isValidPhoneNum(tel):  
                        errors.append('El número de teléfono (' + tel + ') del centro: ' + dencen + ' es inválida.')    

                #Postal code error detection
                cpcen = None
                if 'cpcen' in item:
                    cpcen = item['cpcen']
                    if not validations.isValidPostalCode(cpcen):
                        errors.append('El código postal (' + cpcen + ') del centro: ' + dencen + ' es inválido.')

                localidad = {'codigo': item['cpcen'], 'nombre': item['loccen']}
                provincia = {'codigo': '30', 'nombre': 'Murcia'}   

                data_model = DataModel(
                    nombre=dencen,
                    tipo=titularidad,
                    direccion=domcen,
                    codigo_postal=item['cpcen'],
                    longitud=lon,
                    latitud=lat,
                    telefono=tel,
                    descripcion=item['presentacionCorta'],
                    localidad=localidad,
                    provincia=provincia
                )

                data.append(data_model)

        return data, errors
    
