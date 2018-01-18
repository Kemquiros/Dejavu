import raza
from avatar import Avatar

class Cazador(Avatar):
  imagen = "static/img/tile/selection/Cazador.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getCazador()    
    self.init2(molde)