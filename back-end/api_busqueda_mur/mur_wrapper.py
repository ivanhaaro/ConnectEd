import json

class MURWrapper:

    def getJSON(self):

        file_path = 'MUR.json'
        
        with open(file_path, 'r', encoding = 'utf-8') as json_file:

            data = json.load(json_file)
            return data