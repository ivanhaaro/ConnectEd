import json
import xml.etree.ElementTree as ET

class CATWrapper:

    def getJSON(self):

        file_path = 'CAT.xml'
        
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Lista para almacenar los diccionarios de cada elemento
        data = []

        # Recorrer los elementos 'row' dentro de 'response'
        for row in root.findall('.//row'):
            
            # Diccionario para almacenar los datos de cada elemento 'row'
            row_data = {}

            # Recorrer los elementos dentro de cada 'row'
            for element in row:
                row_data[element.tag] = element.text

            if 'row' in row_data:
                continue

            # Agregar el diccionario a la lista
            data.append(row_data)

        # Devolver la lista como JSON
        return data
            