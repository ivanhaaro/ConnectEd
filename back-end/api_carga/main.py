from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sys
sys.path.append('..')

from extractors.cat_extractor import CATExtractor
from extractors.cv_extractor import CVExtractor
from extractors.mur_extractor import MURExtractor
from database.db_connector import DBConnector

app = FastAPI(title='ConnectEd Carga API', version='0.0.1', description='API de carga del almacén de datos de ConnectEd', )

# Configuración de CORS para permitir cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Función para cargar datos en la base de datos
def load_database(data_list):
    db = DBConnector("../../database")
    db.create_table()
    db.insert_data(data_list)

# Función para cargar datos en la base de datos para todas las regiones
def load_all_database():

    # Crear instancias de extractores para cada región
    cv_extractor = CVExtractor()
    mur_extractor = MURExtractor()
    cat_extractor = CATExtractor()

    # Extraer datos de cada región
    data_list, errors = mur_extractor.extract_data()

    data_listCV, errorsCV = cv_extractor.extract_data()
    data_list.extend(data_listCV)
    errors.extend(errorsCV)

    data_listCAT, errorsCAT = cat_extractor.extract_data()
    data_list.extend(data_listCAT)
    errors.extend(errorsCAT)

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    # Insertar datos en la base de datos
    load_database(data_list)

    return data_list, errors


# Ruta para cargar datos en la base de datos para la Región de Murcia
@app.get('/loadDataMUR')
async def load_database_data():

    mur_extractor = MURExtractor()
    data_list, errors = mur_extractor.extract_data()

    # Guardar errores en un archivo 'errors.txt'
    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    # Cargar datos en la base de datos
    load_database(data_list)

    return {"message": f"Datos cargados correctamente para la Región de Murcia",
            "defectos": errors}



# Ruta para cargar datos en la base de datos para la Comunidad Valenciana
@app.get('/loadDataCV')
async def load_database_data():

    cv_extractor = CVExtractor()
    data_list, errors = cv_extractor.extract_data()

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    load_database(data_list)

    return {"message": f"Datos cargados correctamente para la Comunidad Valenciana",
            "defectos": errors}


# Ruta para cargar datos en la base de datos para Cataluña
@app.get('/loadDataCAT')
async def load_database_data():

    cat_extractor = CATExtractor()
    data_list, errors = cat_extractor.extract_data()

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    load_database(data_list)

    return {"message": f"Datos cargados correctamente para Cataluña",
            "defectos": errors}


# Ruta para cargar datos en la base de datos para todas las regiones
@app.get('/loadDataALL')
async def load_database_data():

    data_list, errors = load_all_database()

    with open('errors.txt', 'w') as file:
        for error in errors:
            print(error, file=file)

    load_database(data_list)

    return {"message": f"Datos cargados correctamente para todas las regiones",
            "defectos": errors}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
