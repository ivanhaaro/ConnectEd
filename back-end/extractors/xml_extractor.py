import xml.etree.ElementTree as ET
from models.data_model import DataModel

class XMLExtractor:
    def extract_data(self, file_path):
        data = []
        tree = ET.parse(file_path)
        root = tree.getroot()
        for item in root: 
            # Extract data from XML and create DataModel objects
            localidad_element = item.find('localidad')
            provincia_element = item.find('provincia')
            localidad = {'codigo': localidad_element.find('codigo').text, 'nombre': localidad_element.find('nombre').text}
            provincia = {'codigo': provincia_element.find('codigo').text, 'nombre': provincia_element.find('nombre').text}
            data_model = DataModel(
                nombre=item.find('nombre').text,
                tipo=item.find('tipo').text,
                direccion=item.find('direccion').text,
                codigo_postal=item.find('codigo_postal').text,
                longitud=item.find('longitud').text,
                latitud=item.find('latitud').text,
                telefono=item.find('telefono').text,
                descripcion=item.find('descripcion').text,
                localidad=localidad,
                provincia=provincia
            )
            data.append(data_model)
        return data
