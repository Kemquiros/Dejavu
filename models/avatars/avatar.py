from equipo import Equipo

class Avatar:
  
  def __init__(self):
    self.jugador = None
    self.raza = None
    self.ataque = None
    self.destreza = None
    self.dano = None
    self.defensa = None    
    self.vida = None
    self.movimiento = None
    self.equipo = Equipo()
    self.mochila = []
    self.monedas = 0
    self.herramientas = 0
    self.reliquias = []
    self.propiedades = {
      "castillos" : [],
      "aldeas" : []
    }
    self.ubicacion = {"x":None,"y":None}
    
  def init2(self,molde):
    self.raza = molde["nombre"]    
    self.ataque = molde["ataque"]    
    self.destreza = molde["destreza"]
    self.dano = molde["dano"]
    self.defensa = molde["defensa"]    
    self.vida = molde["vida"]
    self.movimiento = molde["movimiento"]
    self.movimientoMax = molde["movimiento"]
    self.vidaMax = molde["vida"]
    
  def setJugador(self,jugador):
    self.jugador = jugador
    
  def asignarPrimerCastillo(self,castillo):
    self.agregarCastillo(castillo)
    self.ubicacion["x"] = castillo.columna
    self.ubicacion["y"] = castillo.fila
    
  def agregarCastillo(self,castillo):
    castillo.propietario = self.jugador
    self.propiedades["castillos"].append(castillo)
    
  def toJSON(self):
    return {
      "raza": self.raza,
      "ataque" : self.ataque,
      "destreza" : self.destreza,
      "dano" : self.dano,
      "defensa" : self.defensa,
      "vida" : self.vida,
      "movimiento" : self.movimiento,
      "equipo" : self.equipo.toJSON(),      
      "mochila" : self.mochila,
      "monedas" : self.monedas,
      "herramientas" : self.herramientas,      
      "reliquias" : self.reliquias,
      "propiedades" : self.propiedades
    }
    