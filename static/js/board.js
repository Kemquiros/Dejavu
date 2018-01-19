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
      images = cargarImagenes(datos);
      setTimeout(relojDibujar, 1500);
  });
  //Establecer timer para actualizar el tiempo
});

function relojDibujar(){
   iniciarDatos(datos);
   establecerListener();
   dibujarTablero(datos);
   dibujarAvatares(datos);
   centrarCamara(datos);
}

function iniciarDatos(data){
   capa1 = document.getElementById("layer1");
   contexto1 = capa1.getContext("2d");
   capa2 = document.getElementById("layer2");
   contexto2 = capa2.getContext("2d");
   capa3 = document.getElementById("layer3");
   contexto3 = capa3.getContext("2d");


   nroFilas = data.nroFil;
   nroColumnas = data.nroCol;

   tamCol = data.tamCol;
   tamFil = data.tamFil;

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

function dibujarTablero(data){
  //Mapa
  var M = [data.mapa1,data.mapa2];
  var V = [data.visual1,data.visual2];
  var C = [contexto1,contexto2];

  for(c=0; c < C.length; c++){
    //Dibujar capa
    var mapa = M[c];
    var visual = V[c];
    var contexto = C[c];
    for(i=0; i<nroColumnas; i++){
      for(j=0 ; j<nroFilas; j++){
        if(mapa[j][i]!=0){
          var tile = data.tiles[mapa[j][i]];
          var baldosa = tile[visual[j][i]];
          if(baldosa === undefined){console.log("i:",i,"  j:",j,"  c:",c," mapa[j][i]:",mapa[j][i]," visual[j][i]:",visual[j][i]);}
          contexto.drawImage(images[tile['path']], baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);
        }
      }
    }
  }
}

function dibujarAvatares(data){
   //Avatares
   var M = [data.mapa3];
   var V = [data.visual3];
   var C = [contexto3];

   for(c=0; c < C.length; c++){
     //Dibujar capa
     var mapa = M[c];
     var visual = V[c];
     var contexto = C[c];
     for(i=0; i<nroColumnas; i++){
       for(j=0 ; j<nroFilas; j++){
         if(mapa[j][i]!=0){
           var tile = data.avatares[mapa[j][i]];
           var baldosa = tile[visual[j][i]];
           if(baldosa === undefined){console.log("i:",i,"  j:",j,"  c:",c," mapa[j][i]:",mapa[j][i]," visual[j][i]:",visual[j][i]);}
           contexto.drawImage(images[tile['path']], baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);
         }
       }
     }
   }
}

function centrarCamara(data){
   var ubicacion = data.ubicacion;
   //Ubicacion del personaje
   var delta = (-1)*ubicacion['x']* tamCol;
   var gamma = (-1)*ubicacion['y']* tamCol;
   //Se ubica el personaje en la pantalla
   delta += contenedorCanvas.clientWidth / 2;
   gamma += contenedorCanvas.clientHeight / 2;

   if( marginLeft + delta > 0 ){
      //Se sale por la izquierda
      marginLeft = 0;
   }else if( marginLeft + delta < (-1)*(maxDespX) ){
      //Se sale por la derecha
      marginLeft = maxDespX;
   }else{
      marginLeft += delta;
   }

   if( marginTop + gamma > 0 ){
      //Se sale por arriba
      marginTop = 0;
   }else if( marginTop + gamma < (-1)*(maxDespY) ){
      //Se sale por abajo
      marginTop = maxDespY;
   }else{
      marginTop += gamma;
   }

   capa1.style.marginLeft = marginLeft + "px";
   capa2.style.marginLeft = marginLeft + "px";
   capa3.style.marginLeft = marginLeft + "px";

   capa1.style.marginTop = marginTop + "px";
   capa2.style.marginTop = marginTop + "px";
   capa3.style.marginTop = marginTop + "px";

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
            capa1.style.marginLeft = marginLeft + "px";
            capa2.style.marginLeft = marginLeft + "px";
            capa3.style.marginLeft = marginLeft + "px";
         }
         if( ( marginTop + gamma <= 0 ) && ( marginTop + gamma >= (-1)*(maxDespY) ) ){
            marginTop += gamma;
            capa1.style.marginTop = marginTop + "px";
            capa2.style.marginTop = marginTop + "px";
            capa3.style.marginTop = marginTop + "px";
         }

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

function cargarImagenes(data){
  resul = {};
  //Por cada llave en tiles
  for (key in data.tiles){
    //Verifica que la llave tenga contenido
    if(data.tiles[key] != null){
      //Si la llave no esta en resul
      if (!(data.tiles[key]['path'] in resul)){
        var image = new Image();
        image.src = data.tiles[key]['path'];
        //Agrega un nuevo resultado
        resul[data.tiles[key]['path']] = image;
      }
    }
  }
  //Por cada llave en avatares
  for (key in data.avatares){
    //Verifica que la llave tenga contenido
    if(data.avatares[key] != null){
      //Si la llave no esta en resul
      if (!(data.avatares[key]['path'] in resul)){
        var image = new Image();
        image.src = data.avatares[key]['path'];
        //Agrega un nuevo resultado
        resul[data.avatares[key]['path']] = image;
      }
    }
  }
  return resul;
}
