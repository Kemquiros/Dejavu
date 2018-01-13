import raza
from avatar import Avatar

class Vampiro(Avatar):

  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getVampiro()    
    self.raza = molde["nombre"]
    self.ataque = molde["ataque"]
    self.destreza = molde["destreza"]
    self.dano = molde["dano"]
    self.defensa = molde["defensa"]
    self.vida = molde["vida"]
    self.movimiento = molde["movimiento"]