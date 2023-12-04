import sqlite3

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
                codigo_postal INT NOT NULL,
                longitud DOUBLE NOT NULL,
                latitud DOUBLE NOT NULL,
                telefono INT,
                descripcion VARCHAR(120),
                en_localidad INT NOT NULL,
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
                INSERT INTO Centro_Educativo (nombre, tipo, direccion, 
                        codigo_postal, longitud, latitud, telefono, descripcion, en_localidad)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                item.nombre, item.tipo, item.direccion, item.codigo_postal,
                item.longitud, item.latitud, item.telefono, item.descripcion, localidad_id
            ))
            self.conn.commit()

        cursor.close()


