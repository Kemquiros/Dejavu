datos = null;
images = null;
$( window ).on('load',function() {
  //Dibujar capas
  jQuery.get('/mapa', function(data, status){
      datos = data;
      images = cargarImagenes(datos);
      setTimeout(relojDibujarTablero, 1500);

  });
  //Establecer timer para actualizar el tiempo
});

function relojDibujarTablero(){
  dibujarTablero(datos);
}

function dibujarTablero(data){

  var capa1 = document.getElementById("layer1");
  var contexto1 = capa1.getContext("2d");
  var capa2 = document.getElementById("layer2");
  var contexto2 = capa2.getContext("2d");
  var capa3 = document.getElementById("layer3");
  var contexto3 = capa3.getContext("2d");

  var nroFilas = data.nroFil;
  var nroColumnas = data.nroCol;

  var tamCol = data.tamCol;
  var tamFil = data.tamFil;

  capa1.width = nroColumnas * tamCol;
  capa1.height = nroFilas * tamFil;
  capa2.width = capa1.width;
  capa2.height = capa1.height;
  capa3.width = capa1.width;
  capa3.height = capa1.height;

  var M = [data.mapa1,data.mapa2,data.mapa3];
  var V = [data.visual1,data.visual2,data.visual3];
  var C = [contexto1,contexto2,contexto3];

  for(c=0; c < C.length; c++){
    //Dibujar capa
    var mapa = M[c];
    var visual = V[c];
    var contexto = C[c];
    for(i=0; i<nroColumnas; i++){
      for(j=0 ; j<nroFilas; j++){
        if(mapa[j][i]!=0){
           tile = null
           if(c <= 1){
             var tile = data.tiles[mapa[j][i]];
          }else if(c==2){
             var tile = data.avatares[mapa[j][i]];
          }

          var baldosa = tile[visual[j][i]];
          if(baldosa === undefined){console.log("i:",i,"  j:",j,"  c:",c," mapa[j][i]:",mapa[j][i]," visual[j][i]:",visual[j][i]);}
          contexto.drawImage(images[tile['path']], baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);
        }
      }
    }
  }
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
