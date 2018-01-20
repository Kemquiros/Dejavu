var datos = null;
var images = null;
var nroFilas = null;
var nroColumnas = null;
var tamCol = null;
var tamFil = null;
//variables canvas
var contenedorCanvas;
var capa1 = null;
var contexto1 = null;
var capa2 = null;
var contexto2 = null;
var capa3 = null;
var contexto3 = null;
//Variables movimiento
var draggin = false;
var lastX;
var lastY;
var marginLeft = 0;
var marginTop = 0;
var maxDespX;
var maxDespY;


$( window ).on('load',function() {
  //Dibujar capas
  jQuery.get('/mapa', function(data, status){
      datos = data;
      images = cargarImagenes();
      setTimeout(relojDibujar, 1500);
  });
  //Establecer timer para actualizar el tiempo
});

function relojDibujar(){
   verMiAvatar();
   iniciarDatos();
   establecerListener();
   dibujarTablero();
   dibujarAvatares();
   centrarCamara();
}

function iniciarDatos(){
   capa1 = document.getElementById("layer1");
   contexto1 = capa1.getContext("2d");
   capa2 = document.getElementById("layer2");
   contexto2 = capa2.getContext("2d");
   capa3 = document.getElementById("layer3");
   contexto3 = capa3.getContext("2d");


   nroFilas = datos.nroFil;
   nroColumnas = datos.nroCol;

   tamCol = datos.tamCol;
   tamFil = datos.tamFil;

   capa1.width = nroColumnas * tamCol;
   capa1.height = nroFilas * tamFil;
   capa2.width = capa1.width;
   capa2.height = capa1.height;
   capa3.width = capa1.width;
   capa3.height = capa1.height;

   contenedorCanvas = $('#contenedor-canvas')[0];
   maxDespX = capa1.width - contenedorCanvas.clientWidth;
   maxDespY = capa1.height- contenedorCanvas.clientHeight;
}

function limpiarTablero(){
   contexto1.clearRect(0, 0, capa1.width, capa1.height);
   contexto2.clearRect(0, 0, capa1.width, capa1.height);
   contexto3.clearRect(0, 0, capa1.width, capa1.height);
}

function dibujarTablero(){
   limpiarTablero();
  //Mapa
  var M = [datos.mapa1,datos.mapa2];
  var V = [datos.visual1,datos.visual2];
  var C = [contexto1,contexto2];

  for(c=0; c < C.length; c++){
    //Dibujar capa
    var mapa = M[c];
    var visual = V[c];
    var contexto = C[c];
    for(i=0; i<nroColumnas; i++){
      for(j=0 ; j<nroFilas; j++){
        if(mapa[j][i]!=0){
          var tile = datos.tiles[mapa[j][i]];
          var baldosa = tile[visual[j][i]];
          if(baldosa === undefined){console.log("i:",i,"  j:",j,"  c:",c," mapa[j][i]:",mapa[j][i]," visual[j][i]:",visual[j][i]);}
          contexto.drawImage(images[tile['path']], baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);
        }
      }
    }
  }
}

function dibujarAvatares(){
   //Avatares
   var M = [datos.mapa3];
   var V = [datos.visual3];
   var C = [contexto3];

   for(c=0; c < C.length; c++){
     //Dibujar capa
     var mapa = M[c];
     var visual = V[c];
     var contexto = C[c];
     for(i=0; i<nroColumnas; i++){
       for(j=0 ; j<nroFilas; j++){
         if(mapa[j][i]!=0){
           var tile = datos.avatares[mapa[j][i]];
           var baldosa = tile[visual[j][i]];
           if(baldosa === undefined){console.log("i:",i,"  j:",j,"  c:",c," mapa[j][i]:",mapa[j][i]," visual[j][i]:",visual[j][i]);}
           contexto.drawImage(images[tile['path']], baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);
         }
       }
     }
   }
}

function centrarCamara(){
   var ubicacion = datos.ubicacion;
   //Ubicacion del personaje
   var delta = (-1)*ubicacion['x']* tamCol;
   var gamma = (-1)*ubicacion['y']* tamCol;
   //Se ubica el personaje en la pantalla
   //Primero: se asume el canvas
   delta += contenedorCanvas.clientWidth / 2;
   gamma += contenedorCanvas.clientHeight / 2;
   //Segundo: se asume la baldosa
   delta -= tamCol / 2;
   gamma -= tamFil / 2;

   if( delta > 0 ){
      //Se sale por la izquierda
      marginLeft = 0;
   }else if( delta < (-1)*(maxDespX) ){
      //Se sale por la derecha
      marginLeft = (-1)*maxDespX;
   }else{
      marginLeft = delta;
   }

   if( gamma > 0 ){
      //Se sale por arriba
      marginTop = 0;
   }else if( gamma < (-1)*(maxDespY) ){
      //Se sale por abajo
      marginTop = (-1)*maxDespY;
   }else{
      marginTop = gamma;
   }

   moverMargenes();

}

function moverMargenes(){
   capa1.style.marginLeft = marginLeft + "px";
   capa2.style.marginLeft = marginLeft + "px";
   capa3.style.marginLeft = marginLeft + "px";

   capa1.style.marginTop = marginTop + "px";
   capa2.style.marginTop = marginTop + "px";
   capa3.style.marginTop = marginTop + "px";
}

function aumentarTablero(){
   var proporcionX = marginLeft/datos.tamCol;
   var proporcionY = marginTop/datos.tamFil;
   datos.tamCol = datos.tamCol + 20;
   datos.tamFil = datos.tamFil + 20;
   iniciarDatos();
   dibujarTablero();
   dibujarAvatares();

   marginLeft = proporcionX * datos.tamCol;
   marginTop = proporcionY * datos.tamFil;

   if( marginLeft > 0 ){
      //Se sale por arriba
      marginLeft = 0;
   }else if( marginLeft < (-1)*(maxDespX) ){
      //Se sale por abajo
      marginLeft = (-1)*maxDespX;
   }
   if( marginTop > 0 ){
      //Se sale por arriba
      marginTop = 0;
   }else if( marginTop < (-1)*(maxDespY) ){
      //Se sale por abajo
      marginTop = (-1)*maxDespY;
   }

   moverMargenes();
}


function disminuirTablero(){
   var proporcionX = marginLeft/datos.tamCol;
   var proporcionY = marginTop/datos.tamFil;

   datos.tamCol = datos.tamCol - 20;
   datos.tamFil = datos.tamFil - 20;
   iniciarDatos();
   dibujarTablero();
   dibujarAvatares();

   marginLeft = proporcionX * datos.tamCol;
   marginTop = proporcionY * datos.tamFil;

   if( marginLeft > 0 ){
      //Se sale por arriba
      marginLeft = 0;
   }else if( marginLeft < (-1)*(maxDespX) ){
      //Se sale por abajo
      marginLeft = (-1)*maxDespX;
   }
   if( marginTop > 0 ){
      //Se sale por arriba
      marginTop = 0;
   }else if( marginTop < (-1)*(maxDespY) ){
      //Se sale por abajo
      marginTop = (-1)*maxDespY;
   }

   moverMargenes();
}


function establecerListener(){

   function presionaMouse(e){
      var evt = e;
      draggin = true;
      lastX = evt.clientX;
      lastY = evt.clientY;
      e.preventDefault();
   }
   function sueltaMouse(e){
      draggin = false;
   }
   function saleMouse(e){
      draggin = false;
   }
   function mueveMouse(e){
      var evt = e;
      if(draggin){
         var delta = evt.clientX - lastX;
         var gamma = evt.clientY - lastY;

         lastX = evt.clientX;
         lastY = evt.clientY;

         if( ( marginLeft + delta <= 0 ) && ( marginLeft + delta >= (-1)*(maxDespX) ) ){
            marginLeft += delta;
         }
         if( ( marginTop + gamma <= 0 ) && ( marginTop + gamma >= (-1)*(maxDespY) ) ){
            marginTop += gamma;
         }

         moverMargenes();

      }
   }

   capa1.addEventListener('mousedown', presionaMouse);
   capa2.addEventListener('mousedown', presionaMouse);
   capa3.addEventListener('mousedown', presionaMouse);

   capa1.addEventListener('mouseup', sueltaMouse);
   capa2.addEventListener('mouseup', sueltaMouse);
   capa3.addEventListener('mouseup', sueltaMouse);

   capa1.addEventListener('onmouseout', saleMouse);
   capa2.addEventListener('onmouseout', saleMouse);
   capa3.addEventListener('onmouseout', saleMouse);

   capa1.addEventListener('mousemove', mueveMouse);
   capa2.addEventListener('mousemove', mueveMouse);
   capa3.addEventListener('mousemove', mueveMouse);
}

function cargarImagenes(){
  resul = {};
  //Por cada llave en tiles
  for (key in datos.tiles){
    //Verifica que la llave tenga contenido
    if(datos.tiles[key] != null){
      //Si la llave no esta en resul
      if (!(datos.tiles[key]['path'] in resul)){
        var image = new Image();
        image.src = datos.tiles[key]['path'];
        //Agrega un nuevo resultado
        resul[datos.tiles[key]['path']] = image;
      }
    }
  }
  //Por cada llave en avatares
  for (key in datos.avatares){
    //Verifica que la llave tenga contenido
    if(datos.avatares[key] != null){
      //Si la llave no esta en resul
      if (!(datos.avatares[key]['path'] in resul)){
        var image = new Image();
        image.src = datos.avatares[key]['path'];
        //Agrega un nuevo resultado
        resul[datos.avatares[key]['path']] = image;
      }
    }
  }
  return resul;
}
