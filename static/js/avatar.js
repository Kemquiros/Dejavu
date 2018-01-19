var jugador;
var equipo;
var inventario;

function verAvatar(){
   //jQuery.get('/juego/avatar', function(data, status){
      //jugador = data;
      //$(#panel-nombre).text(jugador.nombre+" / "+jugador.avatar.raza);
      //$(#img1).('src', jugador.avatar.imagen);
      $( "#vista-avatar" ).show();
      $( "#vista-equipo" ).hide();
      $( "#vista-inventario" ).hide();
      $( "#vista-propiedades" ).hide();
      $( "#vista-jugar" ).hide();
      $( "#vista-estado" ).hide();
   //});
}
function verEquipo(){
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).show();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
}
function verInventario(){
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).show();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
}
function verPropiedades(){
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).show();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).hide();
}
function verJugar(){
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).show();
   $( "#vista-estado" ).hide();
}
function verEstado(){
   $( "#vista-avatar" ).hide();
   $( "#vista-equipo" ).hide();
   $( "#vista-inventario" ).hide();
   $( "#vista-propiedades" ).hide();
   $( "#vista-jugar" ).hide();
   $( "#vista-estado" ).show();
}
function consultarActualizacion(){

}
