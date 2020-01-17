import models.avatars.raza as raza
from .avatar import Avatar

class Hechizero(Avatar):

  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getHechizero()
    self.init2(molde)
