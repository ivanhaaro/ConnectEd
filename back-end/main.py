from extractors.xml_extractor import XMLExtractor
from extractors.csv_extractor import CSVExtractor
from extractors.json_extractor import JSONExtractor

def main():
    # Ruta al archivo CSV que deseas procesar
    csv_file_path = 'back-end/CV.csv'
    json_file_path = 'back-end/MUR.json'
    xml_file_path = 'back-end/CAT.xml'

    # Crear una instancia del extractor de CSV
    csv_extractor = CSVExtractor()
    json_extractor = JSONExtractor()
    xml_extractor = XMLExtractor()

    # Extraer los datos del archivo CSV
    data_list, errors = csv_extractor.extract_data(csv_file_path)
    data_listJSON, errorsJSON = json_extractor.extract_data(json_file_path)
    data_list.append(data_listJSON)
    errors.append(errorsJSON)
    data_listXML, errorsXML = xml_extractor.extract_data(xml_file_path)
    data_list.append(data_listXML)
    errors.append(errorsXML)

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
    

    # for error in errors:
    #     print(error)


if __name__ == "__main__":
    main()
