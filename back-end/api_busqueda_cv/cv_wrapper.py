from geoapiservice.google_maps_service import GoogleMapsGeocoder
import csv

class CVWrapper:

    def getJSON(self):
        geo_service = GoogleMapsGeocoder('AIzaSyDI0bLLisjbLkXAjUD52_g_sZKGqGGn1jQ')

        # Ruta del archivo CSV y JSON
        archivo_csv = 'CV.csv'

        # Leer el archivo CSV y convertirlo a formato JSON
        with open(archivo_csv, 'r', encoding='utf-8') as csv_file:
            # Configurar el lector CSV
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            
            # Convertir a lista de diccionarios
            data = [row for row in csv_reader]

            # Agregar latitud y longitud a cada diccionario
            for item in data:
                direccion = f"{item['DIRECCION']} {item['NUMERO']}, {item['LOCALIDAD']}, {item['PROVINCIA']}, Spain"
                latitud, longitud = geo_service.getlatlong(direccion)

                item['LATITUD'] = str(latitud)
                item['LONGITUD'] = str(longitud)

            return data