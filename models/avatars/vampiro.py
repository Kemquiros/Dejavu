import raza
from avatar import Avatar

class Vampiro(Avatar):
  imagen = "static/img/tile/Vampiro.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getVampiro()    
    self.init2(molde)