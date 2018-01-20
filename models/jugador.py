class Jugador:

  def __init__(self,name,icon, tk):
    self.nombre = name
    self.icono = icon
    self.token = tk
    self.avatar = None
    self.partida = None
    self.turno = None

  def setAvatar(self,avt):
    self.avatar = avt
  def setPartida(self,p):
    self.partida = p

  def toJSON(self):
    return {
      "nombre" : self.nombre,
      "icono" : self.icono,
      "turno" : self.turno,
      "avatar" : self.avatar.toJSON()
    }
