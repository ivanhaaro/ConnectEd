from fastapi import FastAPI, HTTPException
from database.db_connector import DBConnector

app = FastAPI(title='ConnectEd Búsqueda API', version='0.0.1', description='API de búsqueda de centros educativos de ConnectEd', )

# Ruta para obtener centros educativos según los parámetros especificados
@app.get('/getEducativeCenters')
async def get_educative_centers(localidad: str | None = None,
                                codigo_postal: str | None = None,
                                provincia: str | None = None,
                                tipo: str | None = None):

    db = DBConnector("../database")  # Instancia de DBConnector para conectarse a la base de datos

    # Realiza una búsqueda en la base de datos según los parámetros proporcionados
    educative_centers = db.search_by(localidad, codigo_postal, provincia, tipo)

    # Convierte los objetos DataModel a diccionarios para la respuesta JSON
    educative_centers_dicts = [center.to_dict() for center in educative_centers]

    return educative_centers_dicts  # Devuelve la lista de centros educativos en formato JSON


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
