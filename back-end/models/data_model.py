class DataModel:
    def __init__(self, nombre, tipo, direccion, codigo_postal, longitud, latitud, telefono, descripcion, localidad, provincia):
        self.nombre = nombre
        self.tipo = tipo
        self.direccion = direccion
        self.codigo_postal = codigo_postal
        self.longitud = longitud
        self.latitud = latitud
        self.telefono = telefono
        self.descripcion = descripcion
        self.localidad = localidad
        self.provincia = provincia

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'tipo': self.tipo,
            'direccion': self.direccion,
            'codigo_postal': self.codigo_postal,
            'longitud': self.longitud,
            'latitud': self.latitud,
            'telefono': self.telefono,
            'descripcion': self.descripcion,
            'localidad': self.localidad,
            'provincia': self.provincia
        }