import json
from models.data_model import DataModel

class JSONExtractor:
    def extract_data(self, file_path):
        data = []
        with open(file_path, 'r') as json_file:
            data_list = json.load(json_file)
            for item in data_list:
                # Create DataModel objects for each JSON item
                localidad = item['localidad']
                provincia = item['provincia']
                data_model = DataModel(
                    nombre=item['nombre'],
                    tipo=item['tipo'],
                    direccion=item['direccion'],
                    codigo_postal=item['codigo_postal'],
                    longitud=item['longitud'],
                    latitud=item['latitud'],
                    telefono=item['telefono'],
                    descripcion=item['descripcion'],
                    localidad=localidad,
                    provincia=provincia
                )
                data.append(data_model)
        return data
