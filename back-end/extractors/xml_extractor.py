import xml.etree.ElementTree as ET
from models.data_model import DataModel

class XMLExtractor:
    def extract_data(self, file_path):
        data = []
        tree = ET.parse(file_path)
        root = tree.getroot()

        for row in root.findall('.//row'):
            # Crear un diccionario para almacenar datos de cada fila
            row_data = {}

            # Iterar sobre los elementos hijos de la fila
            for element in row:
                # Utilizar el nombre del elemento como clave y su texto como valor
                row_data[element.tag] = element.text

            # Crear un objeto DataModel a partir de los datos de la fila
            localidad = {'codigo': '', 'nombre': row_data.get('nom_municipi')}
            provincia = {
                'codigo': row_data.get('codi_postal'), 'nombre': row_data.get('codi_postal')}
            tipo = row_data.get('nom_naturalesa')
            if tipo == 'Privat':
                tipo = 'Privado'
            elif tipo == 'Públic':
                tipo = 'Público'

            data_model = DataModel(
                nombre= row_data.get('denominaci_completa'),
                tipo= tipo,
                codigo_postal=row_data.get('codi_postal'),
                direccion=row_data.get('adre_a'),
                longitud=row_data.get('coordenades_geo_x'),
                latitud=row_data.get('coordenades_geo_y'),
                telefono= '',
                descripcion= '',
                localidad=localidad,
                provincia=provincia,

            )

            # Agregar el objeto DataModel a la lista de datos
            data.append(data_model)

        return data

