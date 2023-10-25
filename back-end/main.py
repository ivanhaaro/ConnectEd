from extractors.csv_extractor import CSVExtractor
from models.data_model import DataModel

def main():
    # Ruta al archivo CSV que deseas procesar
    csv_file_path = 'centros-docentes-de-la-comunitat-valenciana.csv'

    # Crear una instancia del extractor de CSV
    csv_extractor = CSVExtractor()

    # Extraer los datos del archivo CSV
    data_list = csv_extractor.extract_data(csv_file_path)

    # Imprimir los datos extraídos
    for data in data_list:
        print(f"Nombre: {data.nombre}")
        print(f"Tipo: {data.tipo}")
        print(f"Dirección: {data.direccion}")
        print(f"Código Postal: {data.codigo_postal}")
        print(f"Longitud: {data.longitud}")
        print(f"Latitud: {data.latitud}")
        print(f"Teléfono: {data.telefono}")
        print(f"Descripción: {data.descripcion}")
        print(f"Localidad: {data.localidad['nombre']} (Código: {data.localidad['codigo']})")
        print(f"Provincia: {data.provincia['nombre']} (Código: {data.provincia['codigo']})")
        print()

if __name__ == "__main__":
    main()
