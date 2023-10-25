import sqlite3

class DBConnector:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Centro_educativo (
                nombre TEXT,
                tipo  TEXT,
                direccion TEXT,
                codigo_postal SMALLINT,
                longitud DOUBLE,
                latitud DOUBLE,
                telefono TEXT,
                descripcion TEXT
            );
        
            CREATE TABLE IF NOT EXISTS Localidad
            
        """)
        self.conn.commit()

    def insert_data(self, data):
        cursor = self.conn.cursor()
        cursor.executemany("""
            INSERT INTO data (column1, column2, column3)
            VALUES (?, ?, ?)
        """, [(item.column1, item.column2, item.column3) for item in data])
        self.conn.commit()