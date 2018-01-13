class Equipo:
  
  def __init__(self):
    self.casco = None
    self.armadura = None
    self.escudo = None
    self.arma = None
    self.montura = None
    self.discipulo = None
    self.gemas = [None,None,None]
    
  def toJSON(self):
    return {
      "casco" : self.casco,
      "armadura" : self.armadura,
      "escudo" : self.escudo,
      "arma" : self.arma,
      "montura" : self.montura ,
      "discipulo" : self.discipulo,
      "gemas" : self.gemas
    }