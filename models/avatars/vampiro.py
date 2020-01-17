import models.avatars.raza as raza
from .avatar import Avatar

class Vampiro(Avatar):

  def __init__(self):
    Avatar.__init__(self)
    molde = raza.getVampiro()
    self.init2(molde)
