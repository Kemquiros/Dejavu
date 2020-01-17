from .equipo import Equipo

class Avatar(object):

    def __init__(self):
        self.imagen = None
        self.jugador = None
        self.raza = None
        self.ataque = None
        self.destreza = None
        self.dano = None
        self.defensa = None
        self.vidaMax = None
        self.vida = None
        self.movimientoMax = None
        self.movimiento = None
        self.equipo = Equipo()
        self.mochila = []
        self.monedas = 0
        self.herramientas = 0
        self.nroReliquias = 0
        self.nroPropiedades = 0
        self.reliquias = []
        self.propiedades = {
        "castillos" : [],
        "aldeas" : []
        }
        self.ubicacion = {"x":None, "y":None}


    def init2(self, molde):
        self.imagen = molde["imagen"]
        self.raza = molde["nombre"]
        self.ataque = molde["ataque"]
        self.destreza = molde["destreza"]
        self.dano = molde["dano"]
        self.defensa = molde["defensa"]
        self.vida = molde["vida"]
        self.movimiento = molde["movimiento"]
        self.movimientoMax = molde["movimiento"]
        self.vidaMax = molde["vida"]

    def toJSON(self):
        return {
        "imagen" : self.imagen,
        "raza": self.raza,
        "ataque" : self.ataque,
        "destreza" : self.destreza,
        "dano" : self.dano,
        "defensa" : self.defensa,
        "vidaMax" : self.vidaMax,
        "vida" : self.vida,
        "movimientoMax" : self.movimientoMax,
        "movimiento" : self.movimiento,
        "equipo" : self.equipo.toJSON(),
        "mochila" : self.mochila,
        "monedas" : self.monedas,
        "herramientas" : self.herramientas,
        "nroReliquias" : self.nroReliquias,
        "reliquias" : self.reliquias,
        "nroPropiedades" : self.nroPropiedades,
        "propiedades" : self.propiedadesToJSON()
            }

    def setJugador(self, jugador):
        self.jugador = jugador

    def asignarPrimerCastillo(self, castillo):
        self.agregarCastillo(castillo)
        self.ubicacion["x"] = castillo.columna
        self.ubicacion["y"] = castillo.fila

    def agregarCastillo(self, castillo):
        castillo.propietario = self.jugador
        self.propiedades["castillos"].append(castillo)
        self.contarPropiedades()

    def contarPropiedades(self):
        self.nroPropiedades = len(self.propiedades["castillos"]) + len(self.propiedades["aldeas"])

    def propiedadesToJSON(self):
        castillos = []
        aldeas = []
        for c in self.propiedades["castillos"]:
            castillos.append(c.toJSON())
        for a in self.propiedades["aldeas"]:
            castillos.append(a.toJSON())
        return {
                "castillos" : castillos,
                "aldeas" : aldeas
            }
