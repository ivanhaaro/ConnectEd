import csv
from scraper.scraper import CoordinateScraper
from models.data_model import DataModel
from extractors.validations import Validations

class CSVExtractor:
    def extract_data(self, file_path):
        data = []
        errors = []
        validations = Validations()
        scraper = CoordinateScraper()
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')  # Especifica el delimitador utilizado en tu CSV
            for row in csv_reader:
            
                try:

                    # Detect name errors
                    dencen = row['DENOMINACION']
                    if not validations.isValidString(dencen):
                        errors.append('El nombre del centro "' + dencen + '" es inválido.')
                        continue

                    #Postal code error detection
                    if 'CODIGO_POSTAL' in row:
                        cpcen = row['CODIGO_POSTAL']
                        if not validations.isValidPostalCode(cpcen):
                            errors.append('El código postal "' + cpcen + '" del centro: ' + dencen + ' es inválido.')
                            continue
                        if 'LOCALIDAD' in row:
                            localidad = {'codigo': row['CODIGO_POSTAL'], 'nombre': row['LOCALIDAD']}
                        if 'PROVINCIA' in row:
                            provincia = {'codigo': row['CODIGO_POSTAL'][:2], 'nombre': row['PROVINCIA']}
                    else:
                        errors.append('El código postal no existe')
                        continue

                    tipoRegimen=row['REGIMEN']
                    if tipoRegimen == 'PÚB.':
                        tipoRegimen = 'Público'
                    elif tipoRegimen == 'PRIV.':
                        tipoRegimen = 'Privado'
                    elif tipoRegimen == 'PRIV. CONC.':
                        tipoRegimen = 'Concertado'
                    elif tipoRegimen == 'OTROS':
                        tipoRegimen = 'Otros'
                    else:
                        errors.append(f'El tipo {tipoRegimen} es inválido')
                        continue
              
                    #Phone number error detection
                    tel = ''
                    if 'TELEFONO' in row:
                        tel = row['TELEFONO']  
                        if not validations.isValidPhoneNum(tel):  
                            errors.append('El número de teléfono "' + tel + '" del centro: ' + dencen + ' es inválido.')
                            continue

                    # Detect address errors
                    direc = None
                    if 'TIPO_VIA' in row and 'DIRECCION' in row and 'NUMERO' in row:
                        direc = f"{row['TIPO_VIA']} {row['DIRECCION']} {row['NUMERO']}"
                        if not validations.isValidString(direc):
                            errors.append('La dirección "' + direc + '" del centro: ' + dencen + ' es inválida.')
                            continue
                    else:
                        errors.append('La dirección no existe.')
                        continue

                    data_model = DataModel(
                        nombre=dencen,
                        tipo=tipoRegimen,
                        direccion=direc,
                        codigo_postal=cpcen,
                        longitud=0,
                        latitud=0,
                        telefono=tel,
                        descripcion=row['DENOMINACION_ESPECIFICA'],
                        localidad=localidad,
                        provincia=provincia
                    )
                    data_model.longitud, data_model.latitud = scraper.getlatlong(data_model.direccion)
                    print(f"Longitud: {data_model.longitud} Latitud= {data_model.latitud}")
                    data.append(data_model)
                except Exception as e:
                    print(f"Error al procesar la fila")
        return data