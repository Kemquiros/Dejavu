import raza
from avatar import Avatar

class Nigromante(Avatar):
  imagen = "static/img/tile/Nigromante.png"
  
  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getNigromante()    
    self.init2(molde)