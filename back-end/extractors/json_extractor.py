import json
from models.data_model import DataModel

class JSONExtractor:
    def extract_data(self, file_path):
        data = []
        with open(file_path, 'r') as json_file:
            data_list = json.load(json_file)
            for item in data_list:
                # Create DataModel objects for each JSON item
                localidad = {'codigo': '', 'nombre': item['loccen']}
                provincia = {'codigo': '30', 'nombre': 'Murcia'}

                data_model = DataModel(
                    nombre=item['dencen'],
                    tipo=item['titularidad'],
                    direccion=item['domcen'],
                    codigo_postal=item['cpcen'],
                    longitud=0,
                    latitud=0,
                    telefono=0,
                    descripcion=item['presentacionCorta'],
                    localidad=localidad,
                    provincia=provincia
                )
                data.append(data_model)
        return data
