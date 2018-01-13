class Jugador:
  
  def __init__(self,name,icon, tk):
    self.nombre = name
    self.icono = icon
    self.token = tk
    self.avatar = None
    
  def setAvatar(self,avt):
    self.avatar = avt
    
  def toJSON(self):
    return {
      "nombre" : self.nombre,
      "icono" : self.icono,
      "token" : self.token,
      "avatar" : self.avatar.toJSON()
    }