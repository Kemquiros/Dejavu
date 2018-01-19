import raza
from avatar import Avatar

class Demiurgo(Avatar):

  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getDemiurgo()
    self.init2(molde)
