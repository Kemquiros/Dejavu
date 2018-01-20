var jugador = null;
var turnoJugador;
var equipo;
var inventario;

function verMiAvatar() {
      if (jugador === null){
         jQuery.get('/juego/jugador', function(data, status){
            jugador = data;
            actualizarAtributos(jugador.avatar,true);
         });
      }else{
         actualizarAtributos(jugador.avatar,true);
      }
      //$(#img1).('src', jugador.avatar.imagen);
      $( "#vista-avatar" ).show();
      $( "#vista-equipo" ).hide();
      $( "#vista-inventario" ).hide();
      $( "#vista-propiedades" ).hide();
      $( "#vista-jugar" ).hide();
      $( "#vista-estado" ).hide();
      //-----------------------------

      $( "#img1" ).show();
   //});
}
function verEquipo() {
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).show();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
   //-----------------------------
   $( "#panel-nombre" ).text("Equipo");
   $( "#img1" ).hide();
}
function verInventario() {
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).show();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
   //-----------------------------
   $( "#panel-nombre" ).text("Inventario");
   $( "#img1" ).hide();
}
function verPropiedades() {
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).show();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
   //-----------------------------
   $( "#panel-nombre" ).text("Propiedades");
   $( "#img1" ).hide();
}
function verJugar() {
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).show();
   $( "#vista-estado" ).hide();
   //-----------------
   actualizarAtributos(jugador.avatar,true);
   $( "#img1" ).hide();
}
function verEstado() {
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).show();
   //-----------------------------
   $( "#panel-nombre" ).text("Estado partida");
   $( "#img1" ).hide();
}
function verAvatar(imagenIcono) {
   $( "#vista-avatar" ).show();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
   //------------------------------
   var id_orden = imagenIcono.id;
   id_orden = id_orden.split("-")[1];
   jQuery.get('/juego/avatar/'+id_orden, function(data, status){
      actualizarAtributos(data,false);
   });
   $( "#img1" ).show();
}
//True si es para actualizar atributos propios
//False para actualizar atributos de otro jugador
function actualizarAtributos(data,opt) {
   if(opt){
      $( "#panel-nombre" ).text(jugador.nombre+" / "+data.raza);
      $( "#img1" ).attr('src', data.imagen);
   }else{
      $( "#panel-nombre" ).text(data.nombre+" / "+data.raza);
      $( "#img1" ).attr('src', data.imagen);
   }

   //Ataque
   $( ".bar-ataque" ).attr('aria-valuenow', data.ataque);
   $( ".bar-ataque" ).css('width:', (data.ataque/6)*100);
   $( ".bar-ataque" ).text(data.ataque);
   //Destreza
   $( ".bar-destreza" ).attr('aria-valuenow', data.destreza);
   $( ".bar-destreza" ).css('width:', (data.destreza/6)*100);
   $( ".bar-destreza" ).text(data.destreza);
   //Dano
   $( ".bar-dano" ).attr('aria-valuenow', data.dano);
   $( ".bar-dano" ).css('width:', (data.dano/6)*100);
   $( ".bar-dano" ).text(data.dano);
   //Defensa
   $( ".bar-defensa" ).attr('aria-valuenow', data.defensa);
   $( ".bar-defensa" ).css('width:', (data.defensa/6)*100);
   $( ".bar-defensa" ).text(data.defensa);
   //Vida
   $( ".bar-vida" ).attr('aria-valuenow', data.vida);
   $( ".bar-vida" ).attr('aria-valuemax', data.vidaMax);
   $( ".bar-vida" ).css('width:', (data.vida/data.vidaMax)*100);
   $( ".bar-vida" ).text(data.vida);
   //Movimiento
   $( ".bar-movimiento" ).attr('aria-valuenow', data.movimiento);
   $( ".bar-movimiento" ).attr('aria-valuemax', data.movimientoMax);
   $( ".bar-movimiento" ).css('width:', (data.movimiento/data.movimientoMax)*100);
   $( ".bar-movimiento" ).text(data.movimiento);
}
function consultarActualizacion() {
   jQuery.get('/juego/actualizar', function(data, status){
      if(data === null){
         window.location.replace("/");
      }else{
         $( "#tiempo-turno" ).text("Tiempo Partida: "+data.tiempoTurno);
         $( "#tiempo-partida" ).text("Tiempo Turno:"+data.tiempoPartida);
         $( "#turno" ).text("Turno #"+data.turno);
         turnoJugador = data.turnoJugador;
      }
   });
}
