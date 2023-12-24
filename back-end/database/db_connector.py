import sqlite3
from models.data_model import DataModel


class DBConnector:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def create_table(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Provincia (
                codigo INTEGER PRIMARY KEY,
                nombre VARCHAR(80) NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Localidad (
                codigo INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(80) NOT NULL UNIQUE,
                en_provincia INT NOT NULL,
                FOREIGN KEY (en_provincia) REFERENCES Provincia(codigo)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Centro_Educativo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(80) NOT NULL,
                tipo TEXT CHECK (tipo IN ("Publico", "Concertado", "Privado", "Otros")) NOT NULL,
                direccion VARCHAR(100) NOT NULL,
                codigo_postal VARCHAR(5) NOT NULL,
                longitud DOUBLE NOT NULL,
                latitud DOUBLE NOT NULL,
                telefono INT,
                descripcion VARCHAR(120),
                en_localidad INT NOT NULL,
                UNIQUE(longitud, latitud),
                FOREIGN KEY (en_localidad) REFERENCES Localidad(codigo)
            )
        """)

        self.conn.commit()

    def insert_data(self, data):
        cursor = self.conn.cursor()

        for item in data:
            # Insert into Provincia
            cursor.execute("""
                INSERT OR IGNORE INTO Provincia (codigo, nombre)
                VALUES (?, ?);
            """, (item.provincia['codigo'], item.provincia['nombre']))
            self.conn.commit()

            # Retrieve provincia_id
            cursor.execute("SELECT codigo FROM Provincia WHERE nombre = ?", (item.provincia['nombre'],))
            provincia_id = cursor.fetchone()[0]

            # Retrieve or insert into Localidad and get localidad_id
            cursor.execute("""
                INSERT OR IGNORE INTO Localidad (nombre, en_provincia)
                VALUES (?, ?)
            """, (item.localidad['nombre'], provincia_id))
            self.conn.commit()

            # Retrieve localidad_id
            cursor.execute("SELECT codigo FROM Localidad WHERE nombre = ?", (item.localidad['nombre'],))
            localidad_id = cursor.fetchone()[0]

            # Insert into Centro_Educativo
            cursor.execute("""
                INSERT OR IGNORE INTO Centro_Educativo (nombre, tipo, direccion, 
                        codigo_postal, longitud, latitud, telefono, descripcion, en_localidad)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item.nombre, item.tipo, item.direccion, item.codigo_postal,
                item.longitud, item.latitud, item.telefono, item.descripcion, localidad_id
            ))
            self.conn.commit()

        cursor.close()

    def search_by(self, localidad, codigo_postal, provincia, tipo):
        cursor = self.conn.cursor()

        # Base query
        query = """
            SELECT ce.*, pr.nombre as provincia_nombre FROM Centro_Educativo ce
            INNER JOIN Localidad lo ON ce.en_localidad = lo.codigo
            INNER JOIN Provincia pr ON lo.en_provincia = pr.codigo
            WHERE
            """

        conditions = []

        # Check each parameter and add conditions accordingly
        if provincia is not None:
            conditions.append(f"pr.nombre = '{provincia}'")
        elif localidad is not None:
            # Select the province name as a subquery
            conditions.append(f"lo.nombre = '{localidad}'")
            query = query.replace("pr.nombre as provincia_nombre",
                                  "(SELECT nombre FROM Provincia WHERE codigo = lo.en_provincia) as provincia_nombre")

        if codigo_postal is not None:
            conditions.append(f"ce.codigo_postal = '{codigo_postal}'")
        if tipo is not None:
            conditions.append(f"ce.tipo = '{tipo}'")

        # Combine the conditions into a single string
        query_conditions = " AND ".join(conditions)
        if query_conditions:
            query += query_conditions
        else:
            # Remove WHERE clause if there are no conditions
            query = query.replace("WHERE", "")

        cursor.execute(query)

        educative_centers = []

        for centroEducativo in cursor.fetchall():
            # Use the province name from the query result if provincia is None
            provincia_name = centroEducativo[-1] if provincia is None else provincia

            educative_centers.append(
                DataModel(
                    nombre=centroEducativo[1],
                    tipo=centroEducativo[2],
                    direccion=centroEducativo[3],
                    codigo_postal=centroEducativo[4],
                    longitud=centroEducativo[5],
                    latitud=centroEducativo[6],
                    telefono=centroEducativo[7],
                    descripcion=centroEducativo[8],
                    localidad=localidad,
                    provincia=provincia_name,
                )
            )

        self.conn.commit()
        return educative_centers
