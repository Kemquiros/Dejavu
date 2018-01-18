import raza
from avatar import Avatar

class Demiurgo(Avatar):
  imagen = "static/img/tile/selection/Demiurgo.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getDemiurgo()    
    self.init2(molde)