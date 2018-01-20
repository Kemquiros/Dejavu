# -*- coding: utf-8 -*-
''' Este el script de entrada para ejecutar el servido de Dejavu-game'''
from flask import Flask
from flask import request #Import flask requests
#from flask import Response #Import flask responses
from flask import render_template #Import flask render templates
#from flask import url_for
from flask import redirect
from flask import session
from flask import jsonify
import random
#import json, urllib #import api modules
from controller import Controller
from models.dejavu import Dejavu

APP = Flask(__name__)
# set the secret key.  keep this really secret:
APP.secret_key = 'A0Zr9sadjl_qe/8j/3yX R~XHH!jmN]LWR/,?RT'

DEJAVU = Dejavu()
CONTROLLER = Controller(DEJAVU)

@APP.route('/')
def index():
    '''Renderiza la página de inicio '''
    icono_aleatorio = random.randint(1, 789)
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
                iconoAleatorio=icono_aleatorio
                )

@APP.route('/login', methods=['POST'])
def do_login():
    '''Función para iniciar sesión '''
    if CONTROLLER.sign_in(request):
        return redirect("/games", code=302)
    return redirect("/", code=302)

@APP.route('/logout', methods=['POST'])
def do_logout():
    '''Función para cerrar sesión '''
    if 'token' in session:
        CONTROLLER.logout()
    return redirect("/", code=302)


@APP.route('/games', methods=['GET'])
def get_games():
    '''Función que renderiza el template para ver
    las partidas existentes '''
    if 'token' in session:
        return render_template(
        'games.html',
        nombre=session['name'],
        icono=session['icon'],
        partidas=DEJAVU.partidas
        )
    return redirect("/", code=302)

@APP.route('/games-list', methods=['GET'])
def get_games_list():
    '''Función que retorna las partidas existentes en un JSON '''
    if 'token' in session:
        resultado = []
        for partida in DEJAVU.partidas.values():
            resultado.append(partida.toJSON())
        return jsonify(resultado)

@APP.route('/new-game', methods=['GET'])
def get_new_game():
    '''Función que renderiza una posible nueva partida '''
    if 'token' in session:
        return render_template('new-game.html',
                               nombre=session['name'],
                               icono=session['icon'])
    return redirect("/games", code=302)

@APP.route('/new-game', methods=['POST'])
def new_game():
    '''Función para confirmar una nueva partida '''
    if 'token' in session:
        CONTROLLER.new_game(request)
        return render_template('join-game.html',
                               nombre=session['name'],
                               icono=session['icon'],
                               razas=DEJAVU.razas)
    return redirect("/games", code=302)

@APP.route('/join-player', methods=['POST'])
def join_player():
    '''Función que renderiza las posibles
    razas a escoger '''
    if 'token' in session:
        CONTROLLER.join_player(request)
        return render_template(
        'join-game.html',
        nombre=session['name'],
        icono=session['icon'],
        razas=DEJAVU.razas,
        master=CONTROLLER.is_master()
        )
    return redirect("/games", code=302)

@APP.route('/join-game', methods=['POST'])
def join_game():
    '''Función que confirma la permanencia de un
    jugador en una partida '''
    if request.method == 'POST':
        CONTROLLER.join_game(request)
        return redirect("/room", code=302)
    return redirect("/games", code=302)

@APP.route('/players', methods=['GET'])
def get_players():
    '''Función que retorna a los jugadores como
    un JSON '''
    if 'token' in session:
        jugadores = CONTROLLER.get_players()
        if jugadores is not None:
            resul = []
            for jugador in jugadores.values():
                resul.append(jugador.toJSON())
            return jsonify(resul)
    return None

@APP.route('/nro-players', methods=['GET'])
def get_nro_players():
    '''Función que retorna el número máximo y actual
    de jugadores en una partida '''
    if 'token' in session:
        partida = DEJAVU.getPartida(session['partida'])
        if partida is None:
            return jsonify({"nro":"x", "nroMax":"cancelada"})
        else:
            return jsonify(
                        {
                            "nro":partida.numeroJugadores,
                            "nroMax":partida.numeroJugadoresMax
                        }
                    )
        return redirect("/games", code=302)

@APP.route('/state', methods=['GET'])
def get_state():
    '''Función que retorna el estado de la partiad
    en un JSON '''
    return jsonify({"state":CONTROLLER.get_state()})

@APP.route('/room', methods=['GET'])
def get_room():
    '''Función utilizada para renderizar
    el template de espera. En este se pueden
    ver los demás participantes '''
    if 'token' in session and 'partida' in session:
        #Si el jugador es el master
        is_master = CONTROLLER.is_master()
        return render_template('room-game.html',
                               nombre=session['name'],
                               icono=session['icon'],
                               master=is_master)
    return redirect("/games", code=302)

@APP.route('/leave-game', methods=['GET'])
def leave_game():
    '''Función utilizada para dejar la partida
    antes de que comience '''
    if 'token' in session:
        if not CONTROLLER.is_master():
            CONTROLLER.leave_game()
    return redirect("/games", code=302)

@APP.route('/cancel-game', methods=['GET'])
def cancel_game():
    '''Función utilizada para que el propietario
    del juego pueda cancelar la partida antes de comenzar '''
    if 'token' in session:
        if CONTROLLER.is_master():
            CONTROLLER.cancel_game()
    return redirect("/games", code=302)

@APP.route('/start', methods=['GET'])
def start_game():
    '''Función que utilizada para avisar al servidor
    para que de comienzo a la partida.
    El servidor cambia el estado de la partida '''
    if 'token' in session and 'partida' in session:
        if CONTROLLER.is_master() and CONTROLLER.getEstadoPartida() == "pendiente":
            CONTROLLER.start()
            return redirect("/board", code=302)
        else:
            return redirect("/room", code=302)
    return redirect("/games", code=302)

@APP.route('/board', methods=['GET'])
def get_board():
    '''Función utilizada para renderizar el template del mapa'''
    if 'token' in session and 'partida' in session:
        partida = DEJAVU.getPartida(session['partida'])
        jugador = None
        if not partida is None:
            if session['name'] in partida.jugadores:
                jugador = partida.getJugador(session['name'])
                print partida.ordenTurno
                if not jugador is None:
                    return render_template('board.html',
                    jugador=jugador.toJSON(),
                    turno=partida.turno,
                    tiempoPartida=partida.getTime(),
                    tiempoTurno=partida.getTimeTurno(),
                    ordenTurno=partida.ordenTurno
                    )
    return redirect("/", code=302)

@APP.route('/mapa', methods=['GET'])
def get_mapa():
    '''Función que retorna el estado
    de las diferentes capas del mapa como un JSON '''
    if 'token' in session and 'partida' in session:
        partida = DEJAVU.getPartida(session['partida'])
        jugador = partida.getJugador(session['name'])
        if not partida is None:
            return jsonify(
            {
            "tamCol" : partida.mapa.data.tamColumnas,
            "tamFil" : partida.mapa.data.tamFilas,
            "nroCol" : partida.mapa.nroFilas,
            "nroFil" : partida.mapa.nroColumnas,
            "tiles" :  partida.mapa.data.tiles,
            "avatares" :  partida.mapa.data.avatares,
            "mapa1" : partida.mapa.mapa1.tolist(),
            "mapa2" : partida.mapa.mapa2.tolist(),
            "mapa3" : partida.mapa.mapa3.tolist(),
            "visual1" : partida.mapa.visual1.tolist(),
            "visual2" : partida.mapa.visual2.tolist(),
            "visual3" : partida.mapa.visual3.tolist(),
            "ubicacion" : jugador.avatar.ubicacion
            }
            )
    return None

'''
Se crea un API para proveer
comunicación al cliente con el servidor
'''

@APP.route('/juego/jugador', methods=['GET'])
def get_jugador():
    if 'token' in session and 'partida' in session:
        jugador = DEJAVU.getJugador(session['token'])
        partida = jugador.partida
        return jsonify(jugador.toJSON())
    return None

@APP.route('/juego/avatar/<int:id_orden>', methods=['GET'])
def get_jugador_avatar(id_orden):
    if 'token' in session and 'partida' in session:
        jugador = DEJAVU.getJugador(session['token'])
        partida = jugador.partida
        if (not jugador is None) and (not partida is None):
            otro_jugador_nombre = partida.ordenTurno[id_orden]['nombre']
            otro_jugador = partida.jugadores[otro_jugador_nombre]
            avatar = otro_jugador.avatar
            return jsonify({
                    "nombre" : otro_jugador.nombre,
                    "raza" : avatar.raza,
                    "imagen" : avatar.imagen,
                    "ataque" : avatar.ataque,
                    "destreza" : avatar.destreza,
                    "dano" : avatar.dano,
                    "defensa" : avatar.defensa,
                    "vidaMax" : avatar.vidaMax,
                    "vida" : avatar.vida,
                    "movimientoMax" : avatar.movimientoMax,
                    "movimiento" : avatar.movimiento,
                    "reliquias" : avatar.nroReliquias,
                    "monedas" : avatar.monedas,
                    "herramientas" : avatar.herramientas,
                    "propiedades" : avatar.nroPropiedades
                })
    return None

@APP.route('/juego/actualizar', methods=['GET'])
def get_actualizar():
    if 'token' in session and 'partida' in session:
        jugador = DEJAVU.getJugador(session['token'])
        if not jugador is None:
            partida = jugador.partida
            return jsonify({
                    "tiempoPartida" : partida.getTime(),
                    "tiempoTurno" : partida.getTimeTurno(),
                    "turno" : partida.turno,
                    "turnoJugador" : partida.jugadorActual
                })
        else:
            redirect("/games", code=302)
    return None

@APP.errorhandler(404)
def page_not_found(error):
    '''Función utilizada para retornar
    un template en caso de no encontrar un manejador
    para la URL solicitada '''
    return render_template('404.html'), 404

if __name__ == '__main__':
    #APP.debug = True #Uncomment to enable debugging
    APP.run(host='0.0.0.0') #Run the Server
