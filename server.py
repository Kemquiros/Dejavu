 # -*- coding: utf-8 -*-

from flask import Flask
from flask import request #Import flask requests
from flask import Response #Import flask responses
from flask import render_template #Import flask render templates
from flask import url_for
from flask import redirect
from flask import session
from flask import jsonify
import random
import json, urllib #import api modules
from controller import Controller
from models.dejavu import Dejavu

app = Flask(__name__)
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr9sadjl_qe/8j/3yX R~XHH!jmN]LWR/,?RT'

dejavu = Dejavu()
controller = Controller(dejavu)

@app.route('/')
def index():
   iconoA = random.randint(1, 789)
   loged = False
   name = None
   icon = None
   
   if 'token' in session:
       loged = True
   if 'name' in session:
      name = session['name']
   if 'icon' in session:
      icon = session['icon']     
   return render_template('index.html',
       nombre=name,
       icono=icon,   
       isLoged=loged,
       iconoAleatorio=iconoA
       )
  
@app.route('/login', methods=['POST'])
def do_login():   
   if controller.sign_in(request): 
      return redirect("/games", code=302)
   return redirect("/", code=302)
  
@app.route('/logout', methods=['POST'])  
def do_logout():
 if 'token' in session:
  controller.logout()
 return redirect("/", code=302)
    

@app.route('/games', methods=['GET'])
def get_games():
   if 'token' in session:
      return render_template(
       'games.html',
       nombre=session['name'],
       icono=session['icon'],
       partidas=dejavu.partidas
      )
   return redirect("/", code=302)
  
@app.route('/games-list',methods=['GET'])
def get_games_list():
  if 'token' in session:  
   resultado = []
   for partida in dejavu.partidas.values():
    resultado.append(partida.toJSON())
   return jsonify(resultado)  

@app.route('/new-game', methods=['GET'])
def get_new_game():
   if 'token' in session:
      return render_template('new-game.html', nombre=session['name'],icono=session['icon'])
   return redirect("/games", code=302)

@app.route('/new-game', methods=['POST'])
def new_game():
   if 'token' in session:
      controller.new_game(request)
      return render_template('join-game.html',nombre=session['name'],icono=session['icon'],razas=dejavu.razas)
   return redirect("/games", code=302)   

@app.route('/join-player', methods=['POST'])
def join_player():
  if 'token' in session:
    controller.join_player(request)
    return render_template(
     'join-game.html',
     nombre=session['name'],
     icono=session['icon'],
     razas=dejavu.razas,
     master=controller.is_master()
    )    
  return redirect("/games", code=302)
                                  
@app.route('/join-game',methods=['POST'])
def join_game():
  if request.method == 'POST':
    controller.join_game(request)
    return redirect("/room", code=302)
  return redirect("/games", code=302)

@app.route('/players',methods=['GET'])
def get_players():
  if 'token' in session:    
   return jsonify(list(jugador.toJSON() for jugador in controller.get_players().values()))

@app.route('/nro-players',methods=['GET'])
def get_nro_players():
  if 'token' in session:
    partida = dejavu.getPartida(session['partida'])
    if partida is None:
     return jsonify({"nro":"x","nroMax":"cancelada"})
    else:
     return jsonify({"nro":partida.numeroJugadores,"nroMax":partida.numeroJugadoresMax})     
  return redirect("/games", code=302)
 
@app.route('/state',methods=['GET'])
def get_state():
 return jsonify({"state":controller.get_state()})

@app.route('/room',methods=['GET'])
def get_room():
  if 'token' in session:
    #Si el jugador es el master
    isMaster = controller.is_master()
    players = controller.get_players()
    return render_template('room-game.html',nombre=session['name'],icono=session['icon'], master=isMaster)
  else:
    return redirect("/games", code=302)
  
@app.route('/leave-game',methods=['GET'])
def leave_game():
  if 'token' in session:
    if not controller.is_master():
      controller.leave_game()
  return redirect("/games", code=302)  
  
@app.route('/cancel-game',methods=['GET'])
def cancel_game():
  if 'token' in session:
    if controller.is_master():
      controller.cancel_game()
  return redirect("/games", code=302)

@app.route('/start',methods=['GET'])
def start_game():
  if 'token' in session:
    if controller.is_master():
      controller.start()
      return redirect("/board", code=302)
    else:
      return redirect("/room", code=302)
  return redirect("/games", code=302)
  
@app.route('/board', methods=['GET'])
def get_board():
  return render_template('board.html')


if __name__ == '__main__':
	#app.debug = True #Uncomment to enable debugging
	app.run(host='0.0.0.0') #Run the Server