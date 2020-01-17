#from avatars import raza
import models.avatars.raza as raza

class Dejavu:
  nroPartidas = 0
  nroJugadores = 0
  partidas = {}
  jugadores = {}
  razas = {}
  
  def __init__(self):
    self.iniciarRazas()
  
  def addJugador(self,jugador):
    if not jugador.token in self.jugadores:
      self.jugadores[jugador.token] = jugador
      self.nroJugadores = self.nroJugadores + 1
    
  def getJugador(self,token):
    if token in self.jugadores:
      return self.jugadores[token]
    return None
    
  def delJugador(self,token):
    if token in self.jugadores:
      del self.jugadores[token]
      self.nroJugadores = self.nroJugadores - 1     
    
  def addPartida(self,partida):
    if not partida.nombre in self.partidas:
      self.partidas[partida.nombre] = partida
      self.nroPartidas = self.nroPartidas + 1
    
  def getPartida(self,nombre):
    if nombre in self.partidas:
      return self.partidas[nombre]  
    return None
    
  def delPartida(self,nombre):
    if nombre in self.partidas:
      del self.partidas[nombre]
      self.nroPartidas = self.nroPartidas - 1     

  def iniciarRazas(self):
    self.razas["0"] = raza.getVampiro()
    self.razas["1"] = raza.getHombreLobo()
    self.razas["2"] = raza.getDemiurgo()
    self.razas["3"] = raza.getCazador()
    self.razas["4"] = raza.getHechizero()
    self.razas["5"] = raza.getNigromante()