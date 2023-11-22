import sqlite3

class DBConnector:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Provincia (
                codigo INT PRIMARY KEY,
                nombre VARCHAR(80) NOT NULL
            );

            CREATE TABLE IF NOT EXISTS Localidad (
                codigo INT PRIMARY KEY,
                nombre VARCHAR(80) NOT NULL,
                en_provincia INT NOT NULL,
                FOREIGN KEY (en_provincia) REFERENCES Provincia(codigo)
            );

            CREATE TABLE IF NOT EXISTS Centro_Educativo (
                id INT PRIMARY KEY,
                nombre VARCHAR(80) NOT NULL,
                tipo ENUM('publico', 'concertado', 'privado', 'otros') NOT NULL,
                dirección VARCHAR(100) NOT NULL,
                codigo_postal INT NOT NULL,
                longitud DOUBLE NOT NULL,
                latitud DOUBLE NOT NULL,
                telefono INT,
                descripción VARCHAR(120),
                en_localidad INT NOT NULL,
                FOREIGN KEY (en_localidad) REFERENCES Localidad(codigo)
            );

            
        """)
        self.conn.commit()

    def insert_dataMurcia(self, data):
        cursor = self.conn.cursor()
        cursor.executemany("""
            INSERT INTO Provincia (nombre)
            VALUES (?, ?);
            INSERT INTO Localidad (codigo, nombre, en_provincia)
            VALUES (?, ?, ?)
            INSERT INTO Centro_Educativo (nombre, tipo, direccion, codigo_postal, longitud, latitud, telefono, descripcion, en_localidad)
        """, [(item.column1, item.column2, item.column3) for item in data])
        self.conn.commit()