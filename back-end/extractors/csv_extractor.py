import csv
from models.data_model import DataModel

class CSVExtractor:
    def extract_data(self, file_path):
        data = []
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                # Create DataModel objects for each row
                localidad = {'codigo': row['CODIGO_POSTAL'], 'nombre': row['LOCALIDAD']}
                provincia = {'codigo': row['CODIGO_POSTAL'][:2], 'nombre': row['PROVINCIA']}
                data_model = DataModel(
                    nombre=row['denominacion'],
                    tipo=row['tipo'],
                    direccion=row['direccion'],
                    codigo_postal=row['codigo_postal'],
                    longitud=row['longitud'],
                    latitud=row['latitud'],
                    telefono=row['telefono'],
                    descripcion=row['descripcion'],
                    localidad=localidad,
                    provincia=provincia
                )
                data.append(data_model)
        return data
