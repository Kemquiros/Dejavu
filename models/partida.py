import time
import random
from map.mapa import Mapa

class Partida:

  def __init__(self,nroJugadores,master,name):
    self.inicioPartida = time.time()
    self.finalPartida = None
    self.inicioTurno = None
    self.finalTurno = None
    self.creador = master
    self.nombre = name
    self.numeroJugadoresMax = nroJugadores
    self.numeroJugadores = 0
    self.jugadores = {}
    self.mapa = None
    self.jugadorActual = None
    self.ordenTurno = None
    self.turno = 0
    self.estado = None

  def crearMapa(self):
    self.mapa = Mapa(self.numeroJugadoresMax)

  def comenzarPartida(self):
    self.estado = "activa"
    self.establecerOrdenTurno()
    self.mapa.ubicarAvatares(self.ordenTurno,self.jugadores)

  def establecerOrdenTurno(self):
    self.ordenTurno = {}
    llaves = self.jugadores.keys()
    while len(self.ordenTurno) < len(llaves):
     nuevo = random.randint(0, len(llaves)-1)
     dict_temp = {
             "nombre" : self.jugadores[llaves[nuevo]].nombre,
             "icono" : self.jugadores[llaves[nuevo]].icono
         }
     if not dict_temp in self.ordenTurno.values():
       self.ordenTurno[len(self.ordenTurno)] = dict_temp
       self.jugadores[llaves[nuevo]].turno = len(self.ordenTurno) - 1
    #Establece a la primera persona
    self.jugadorActual = 0
    self.nuevoTurno()

  def nuevoTurno(self):
    self.finalTurno = time.time() + 30
    self.turno = self.turno + 1



  def siguienteJugador(self):
    self.jugadorActual += 1 % self.numeroJugadores
    if self.jugadorActual == 0:
      self.nuevoTurno()

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

  def getTimeTurno(self):
    return "%02d" % (self.finalTurno - time.time())
