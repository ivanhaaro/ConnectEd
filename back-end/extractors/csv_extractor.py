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
                    localidad = {'codigo': row['CODIGO_POSTAL'], 'nombre': row['LOCALIDAD']}
                    provincia = {'codigo': row['CODIGO_POSTAL'][:2], 'nombre': row['PROVINCIA']}

                    tipoRegimen=row['REGIMEN'],
                    if tipoRegimen == 'PÚB':
                        tipoRegimen = 'Público'
                    elif tipoRegimen == 'PRIV':
                        tipoRegimen = 'Privado'
                    elif tipoRegimen == 'PRIV.CONC.':
                        tipoRegimen = 'Concertado'
                    elif tipoRegimen == 'OTROS':
                        tipoRegimen = 'Otros'
                    else:
                        errors.append('El tipo "' + tipoRegimen + '" es inválido')
                        continue

                    # Detect cod post errors
                    cod = row['CODIGO_POSTAL']
                    if not validations.isValidPostalCode(cod):
                        errors.append('El código postal "' + cod + '" es inválido.')

                    #Phone number error detection
                    tel = row['TELEFONO']
                    if not validations.isValidPhoneNum(tel):  
                        errors.append('El número de teléfono "' + tel + '" es inválido.')

                    data_model = DataModel(
                        nombre=row['DENOMINACION'],
                        tipo=tipoRegimen,
                        direccion=f"{row['TIPO_VIA']} {row['DIRECCION']} {row['NUMERO']}",
                        codigo_postal=cod,
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