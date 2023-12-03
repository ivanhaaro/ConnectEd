import csv
from scraper.scraper import CoordinateScraper
from models.data_model import DataModel

class CSVExtractor:
    def extract_data(self, file_path):
        data = []
        scraper = CoordinateScraper()
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')  # Especifica el delimitador utilizado en tu CSV
            for row in csv_reader:
            
                try:
                    localidad = {'codigo': row['CODIGO_POSTAL'], 'nombre': row['LOCALIDAD']}
                    provincia = {'codigo': row['CODIGO_POSTAL'][:2], 'nombre': row['PROVINCIA']}
                    data_model = DataModel(
                        nombre=row['DENOMINACION'],
                        tipo=row['TIPO_VIA'],
                        direccion=row['DIRECCION'],
                        codigo_postal=row['CODIGO_POSTAL'],
                        longitud=0,
                        latitud=0,
                        telefono=row['TELEFONO'],
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