import raza
from avatar import Avatar

class Hechizero(Avatar):
  imagen = "static/img/tile/selection/Hechizero.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getHechizero()    
    self.init2(molde)