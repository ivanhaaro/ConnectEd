from fastapi import FastAPI, HTTPException, Query

from extractors.xml_extractor import XMLExtractor
from extractors.csv_extractor import CSVExtractor
from extractors.json_extractor import JSONExtractor
from database.db_connector import DBConnector

app = FastAPI(title='ConnectEd API', version='0.0.1', description='The API for educative centers at Spain', )

@app.get('/loadDataBaseData')
async def load_database_data(comunidad: str):

    if comunidad == 'murcia':
        json_extractor = JSONExtractor()
        data_list, errors = json_extractor.extract_data('MUR.json')

    elif comunidad == 'comunidad_valenciana':
        csv_extractor = CSVExtractor()
        data_list, errors = csv_extractor.extract_data('CV.csv')

    elif comunidad == 'cataluña':
        xml_extractor = XMLExtractor()
        data_list, errors = xml_extractor.extract_data('CAT.xml')

    elif comunidad == 'todas':
        data_list, errors = load_all_database()
    
    else:
        raise HTTPException(status_code=500, detail="Comunidad invalida")

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    load_database(data_list)

    return {"message": f"Datos cargados correctamente para {comunidad}",
            "defectos": errors}


def load_database(data_list):
    db = DBConnector("../database")
    db.create_table()
    db.insert_data(data_list)


def load_all_database():
    # Ruta al archivo CSV que deseas procesar
    csv_file_path = 'CV.csv'
    json_file_path = 'MUR.json'
    xml_file_path = 'CAT.xml'

    # Crear una instancia del extractor de CSV
    csv_extractor = CSVExtractor()
    json_extractor = JSONExtractor()
    xml_extractor = XMLExtractor()

    # Extraer los datos de los archivos
    data_list, errors = json_extractor.extract_data(json_file_path)

    data_listCSV, errorsCSV = csv_extractor.extract_data(csv_file_path)
    data_list.extend(data_listCSV)
    errors.extend(errorsCSV)

    data_listXML, errorsXML = xml_extractor.extract_data(xml_file_path)
    data_list.extend(data_listXML)
    errors.extend(errorsXML)

    # Imprimir los datos extraídos
    # for data in data_list:
    #     print(f"Nombre: {data.nombre}")
    #     print(f"Tipo: {data.tipo}")
    #     print(f"Dirección: {data.direccion}")
    #     print(f"Código Postal: {data.codigo_postal}")
    #     print(f"Longitud: {data.longitud}")
    #     print(f"Latitud: {data.latitud}")
    #     print(f"Teléfono: {data.telefono}")
    #     print(f"Descripción: {data.descripcion}")
    #     print(f"Localidad: {data.localidad['nombre']} (Código: {data.localidad['codigo']})")
    #     print(f"Provincia: {data.provincia['nombre']} (Código: {data.provincia['codigo']})")
    #     print()

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    # Insert data into database
    db = DBConnector("../database")
    db.create_table()
    db.insert_data(data_list)

    return data_list, errors

@app.get('/getEducativeCenters')
async def get_eduatcive_centers(localidad: str | None = None,
                            codigo_postal: str | None = None,
                            provincia: str | None = None,
                            tipo: str | None = None):

    db = DBConnector("../database") 

    educative_centers = db.search_by(localidad, codigo_postal, provincia, tipo)

    educative_centers_dicts = [center.to_dict() for center in educative_centers]

    return educative_centers_dicts

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
