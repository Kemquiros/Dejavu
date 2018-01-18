import raza
from avatar import Avatar

class HombreLobo(Avatar):
  imagen = "static/img/tile/Hombre_Lobo.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getHombreLobo()    
    self.init2(molde)