import csv
from models.data_model import DataModel
from selenium.scraper import getlatlong

class CSVExtractor:
    def extract_data(self, file_path):
        data = []
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
                    getlatlong()
                    data.append(data_model)
                except Exception as e:
                    print(f"Error al procesar la fila: {e}")
        return data