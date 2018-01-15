import time
import random
from map.mapa import Mapa

class Partida:
  
  def __init__(self,nroJugadores,master,name):
    self.inicioPartida = time.time()
    self.finalPartida = None    
    self.creador = master
    self.nombre = name
    self.numeroJugadoresMax = nroJugadores
    self.numeroJugadores = 0
    self.jugadores = {}
    self.mapa = None
    self.turnoActual = None
    self.ordenTurno = None
    self.turno = 0
    self.estado = None
    
  def crearMapa(self):
    self.mapa = Mapa(numeroJugadores)
    
  def nuevoTurno(self):
     self.turno = self.turno + 1
     self.turnoActual = 0
     self.ordenTurno = []
     llaves = list[jugadores.keys()]
     while(len(self.ordenTurno)<len(llaves)):
       nuevo = random.randint(0, len(llaves)-1)
       if not llaves[nuevo] in self.ordenTurno:
         self.ordenTurno.append(llaves[nuevo])
       
  
  def addJugador(self,jugador):
    if not jugador.nombre in self.jugadores:
      self.jugadores[jugador.nombre] = jugador
      self.numeroJugadores = self.numeroJugadores + 1
      
  def getJugador(self,nombre):
    if nombre in self.jugadores:
      return self.jugadores[nombre]
    return None
  
  def delJugador(self,nombre):
    if nombre in self.jugadores:
      del self.jugadores[nombre]   
      self.numeroJugadores = self.numeroJugadores - 1
      
  def puedeAddJugador(self):
    return self.numeroJugadores < self.numeroJugadoresMax
   
  def toJSON(self):
   creatorName = None
   if not self.creador is None:
     creatorName = self.creador.nombre
   return {
    "inicioPartida" : self.getTime(),
    "creador" : creatorName,
    "nombre" : self.nombre,
    "numeroJugadoresMax" : self.numeroJugadoresMax,
    "numeroJugadores" : self.numeroJugadores,
    "estado" : self.estado    
   }
  
  def getTime(self):
   seconds = time.time() - self.inicioPartida
   m, s = divmod(seconds, 60)
   h, m = divmod(m, 60)
   return "%d:%02d:%02d" % (h, m, s)
      

    