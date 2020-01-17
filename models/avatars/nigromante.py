import models.avatars.raza as raza
from .avatar import Avatar

class Nigromante(Avatar):

  def __init__(self):
    #super(Nigromante,self).__init__()
    Avatar.__init__(self)
    molde = raza.getNigromante()
    self.init2(molde)
