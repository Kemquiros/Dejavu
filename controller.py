# -*- coding: utf-8 -*-
from flask import session
import hashlib
import re
from models.dejavu import Dejavu
from models.jugador import Jugador
from models.partida import Partida
from models.avatars.vampiro import Vampiro
from models.avatars.hombreLobo import HombreLobo
from models.avatars.demiurgo import Demiurgo
from models.avatars.cazador import Cazador
from models.avatars.hechizero import Hechizero
from models.avatars.nigromante import Nigromante

class Controller:

  def __init__(self,juego):
    self.dejavu = juego

  def sign_in(self,request):
    if request.method == 'POST':
      name = request.form['nombre']
      icon = request.form['ico']
      token = hashlib.sha256(name).hexdigest()

      #El usuario es nuevo en el sistema
      if 'token' in self.dejavu.jugadores:
        return False
      else:
        #Crear usuario en el sistema
        jugador = Jugador(name,icon,token)
        self.dejavu.addJugador(jugador)

        session['token'] = token
        session['name'] = name
        session['icon'] = icon
        return True

  def logout(self):
    if 'token' in session:
      self.leave_game()
      jugador = self.dejavu.getJugador(session['token'])
      if jugador is not None:
        self.dejavu.delJugador(jugador.token)
      for element in ['token','name','icon']:
        if element in session:
          del session[element]

  def new_game(self,request):

    if request.method == 'POST' and 'token' in session:
      numeroJ = int(request.form['numeroJ'])
      nombreP= request.form['nombreP']
      master = self.dejavu.getJugador(session['token'])
      nuevaPartida = Partida(numeroJ,master,nombreP)
      nuevaPartida.estado = "pendiente"
      self.dejavu.addPartida(nuevaPartida)
      session['partida'] = nombreP
      nuevaPartida.crearMapa()

  def leave_game(self):
    if 'token' in session:
      jugador = self.dejavu.getJugador(session['token'])
      if not jugador is None:
        if not jugador.partida is None:
          partida = jugador.partida
          partida.delJugador(jugador.nombre)
          if partida.numeroJugadores == 0 and partida.estado == "activa":
            partida.estado = "terminada"
            self.dejavu.delPartida(jugador.partida.nombre)
          jugador.partida = None
      if 'partida' in session:
        del session['partida']

  def cancel_game(self):
    jugador = self.dejavu.getJugador(session['token'])
    if jugador.partida is not None:
      self.dejavu.delPartida(jugador.partida.nombre)
      self.leave_game()

  def join_player(self,request):
    nombreP = request.form['partida']
    session['partida'] = nombreP

  def join_game(self,request):
    if 'token' in session and 'partida' in session:
      partida = self.dejavu.getPartida(session['partida'])
      jugador = self.dejavu.getJugador(session['token'])
      if (not partida is None) and (not jugador is None):
        #Crear avatar
        idRaza = request.form['raza']
        raza = self.dejavu.razas[str(idRaza)]["nombre"]
        avatar = self.create_avatar(raza)
        avatar.setJugador(jugador)
        if partida.puedeAddJugador():
          jugador.setAvatar(avatar)
          jugador.setPartida(partida)
          partida.addJugador(jugador)
          return True
        else:
          #la partida esta completa
          del session['partida']
    return False


  def is_master(self):
    if 'partida' in session and 'token' in session:
      partida = self.dejavu.getPartida(session['partida'])
      if partida is not None:
        if session['token'] == partida.creador.token:
          return True
    return False

  def get_players(self):
    if 'partida' in session:
      partida = self.dejavu.getPartida(session['partida'])
      if partida is not None:
        return partida.jugadores
    return None

  def get_state(self):
    if 'partida' in session:
      partida = self.dejavu.getPartida(session['partida'])
      if partida is not None:
        return partida.estado
      else:
        return "no existe"
    return None

  def start(self):
    partida = self.dejavu.getPartida(session['partida'])
    partida.comenzarPartida()
    partida.nuevoTurno()

  def getEstadoPartida(self):
    partida = self.dejavu.getPartida(session['partida'])
    return partida.estado

  #----------------------------------------
  #-----------METODOS DEL JUEGO------------
  #----------------------------------------


  def create_avatar(self,raza):
    avatar = None
    if(raza=="Vampiro"):
      avatar = Vampiro()
    elif(raza=="Hombre Lobo"):
      avatar = HombreLobo()
    elif(raza=="Demiurgo"):
      avatar = Demiurgo()
    elif(raza=="Cazador"):
      avatar = Cazador()
    elif(raza=="Hechizero"):
      avatar = Hechizero()
    elif(raza=="Nigromante"):
      avatar = Nigromante()
    return avatar
