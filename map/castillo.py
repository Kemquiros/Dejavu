class Castillo:

    def __init__(self, fil, col):
        self.fila = fil
        self.columna = col
        self.propietario = None
        self.nombre = None
        self.precio = None
    def toJSON(self):
        return {
                "fila" : self.fila,
                "columna" : self.columna,
                "propietario" : self.propietario.nombre,
                "nombre" : self.nombre,
                "precio" : self.precio
            }
