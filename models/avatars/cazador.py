import models.avatars.raza as raza
from .avatar import Avatar

class Cazador(Avatar):

  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getCazador()
    self.init2(molde)
