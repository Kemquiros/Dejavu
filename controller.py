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

  def new_game(self,request):
    if request.method == 'POST':
      numeroJ = int(request.form['numeroJ'])
      nombreP= request.form['nombreP']
      master = self.dejavu.getJugador(session['token'])
      nuevaPartida = Partida(numeroJ,master,nombreP)
      nuevaPartida.estado = "pendiente"
      self.dejavu.addPartida(nuevaPartida)
      session['partida'] = nombreP  
      
  def join_player(self,request):
    nombreP = request.form['partida']
    session['partida'] = nombreP
    
  def join_game(self,request):
    partida = self.dejavu.getPartida(session['partida'])
    jugador = self.dejavu.getJugador(session['token']) 
    #Crear avatar
    idRaza = request.form['raza']
    raza = self.dejavu.razas[str(idRaza)]["nombre"]
    avatar = get_avatar(raza)
    
    if partida.puedeAddJugador():
      jugador.setAvatar(avatar)
      partida.addJugador(jugador)
      return True
    
    session['partida'] = None
    return False
        
      
  def is_master(self):
    partida = self.dejavu.getPartida(session['partida'])
    if session['token'] == partida.creador.token:
      return True
    return False
  
  def get_players(self):
    partida = self.dejavu.getPartida(session['partida'])
    return partida.jugadores
  
  def get_state(self):
    partida = self.dejavu.getPartida(session['partida'])
    if partida is not None:
      return partida.estado 
    return None
  
  def start(self):
    partida = self.dejavu.getPartida(session['partida'])
    partida.estado = "activa"
    
def get_avatar(raza):
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