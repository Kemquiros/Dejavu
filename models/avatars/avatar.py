from equipo import Equipo

class Avatar:
  
  def __init__(self):
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
    