import time

class Partida:
  
  def __init__(self,nroJugadores,master,name):
    self.inicioPartida = time.time()
    self.finalPartida = None    
    self.creador = master
    self.nombre = name
    self.numeroJugadoresMax = nroJugadores
    self.numeroJugadores = 1
    self.jugadores = {}
    self.mapa = None
    self.ordenTurno = None
    self.turno = 0
    self.estado = None
  
  def addJugador(self,jugador):
    if not jugador.nombre in self.jugadores:
      self.jugadores[jugador.nombre] = jugador
      
  def getJugador(self,nombre):
    if nombre in self.jugadores:
      return self.jugadores[nombre]
    return None
  
  def delJugador(self,nombre):
    if nombre in self.jugadores:
      del self.jugadores[nombre]    
      

    