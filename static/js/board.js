
function crearTablero(){
  var capa1 = document.getElementById("layer1");
  var contexto1 = capa1.getContext("2d");
  var capa2 = document.getElementById("layer2");
  var contexto2 = capa2.getContext("2d");  
  var capa3 = document.getElementById("layer3");
  var contexto3 = capa3.getContext("2d");   
  
  var nroJugadores = 6;
  var promMovimiento = 7;
  var nroFilas = nroJugadores * promMovimiento;
  var nroColumnas = nroJugadores * promMovimiento;
  
  var tamCol = 40;
  var tamFil = 40;
  
  var nroOceanosMax = (nroJugadores/4)+1;
  var nroRiosMax = (nroJugadores/2)+1;
    
  
  capa1.width = nroColumnas * tamCol;
  capa1.height = nroFilas * tamFil;
  
  capa2.width = capa1.width;
  capa2.height = capa1.height;
  capa3.width = capa1.width;
  capa3.height = capa1.height;  
  
  var tilesPrado = JSON.parse(getTilesPrado());
  var tilesOceano = JSON.parse(getTilesOceano()); 
  var tilesCamino = JSON.parse(getTilesCamino()); 
  var tilesBosque = JSON.parse(getTilesBosque());
  var tilesMontana = JSON.parse(getTilesMontana());
  
  //Crear la variable mapa
  var mapa = new Array(nroFilas);
  for(i=0; i<nroFilas; i++){
    mapa[i] = new Array(nroColumnas);
  }
  
    var imageTile = new Image();
    imageTile.src = tilesPrado.path;
    imageTile.onload = function() {
      
      //-----Asignar el prado
      for(i=0;i<nroFilas;i++){
        for(j=0 ; j<nroColumnas ;j++){
          mapa[i][j] = "prado";
        }
      }
      
      //-----Asignar oceano          
      var nroOceanos = 0;
      oceanoOcupado = new Array(5);
      for(i=0;i<5;i++){
        oceanoOcupado[i] = 0;
      }
      while(nroOceanos < nroOceanosMax){
          nroOceanos++;
        
          //Establece el tamaño del oceano
          var tamOceano = (promMovimiento/2) * Math.floor((Math.random() * nroJugadores) + 1);
          tamOceano = Math.floor(tamOceano);  
        console.log("tamOceano:",tamOceano);          
        
          //Selecciona 1 de los 5 oceanos
          var puedeContinuar = false;
          var oceano;
          while(!puedeContinuar){
            oceano = Math.floor((Math.random() * 6) + 0) ;
            if(oceanoOcupado[oceano]==0){
               oceanoOcupado[oceano] = 1;
                puedeContinuar = true;
            }
          }
           
         /*
          -------
         |0     1|
         |   4   |
         |3     2|
          -------
         */
        console.log("Oceano#:",oceano);
        var centroOceano = getCentroOceano(oceano,nroFilas,nroColumnas);
        var xCentro = centroOceano[0];
        var yCentro = centroOceano[1];

        
        //Recorre todo el mapa y dibuja el oceano
        //Segun la distancia entre la casilla y el centro del oceano
        for(i=0; i < nroColumnas ;i++){
          for(j=0 ; j < nroFilas;j++){
            //Calcula la distancia
            var distancia = calcularDistancia(i,j,xCentro,yCentro); 
            distancia = Math.sqrt(distancia);
            
            //Obtiene la probabilidad
            var probabilidad = gaussianPDF(0, tamOceano, distancia);//distribution.pdf(distancia);
            //console.log("x: ",i,"  xCentro:",xCentro,"  y:",j,"  yCentro:",yCentro,"  Distancia:",distancia,"  prob:",probabilidad);
            if(Math.random() <= (probabilidad*10)){               
              mapa[j][i] = "oceano";
            }
          }
        }//Recorre todo el mapa para dibujar el oceano        
      }//Mientras no esten completos los oceanos
      
      
      //Aplicar factor morfologico closing
      //closing =  dilatacion -> erosion
                
      //----Dilatacion
      for(i=0;i<3;i++){
        mapa = dilate(mapa, nroFilas,nroColumnas, 3);

        //----Erosion
        mapa = erode(mapa, nroFilas,nroColumnas, 3);
      }
      mapa = erode(mapa, nroFilas,nroColumnas, 3);

      
      
      //-----Asignar rio
      var nroRios = 0;
      while(nroRios<nroRiosMax){
        for(i=0; i<nroColumnas;i++){
          for(j=0 ; j<nroFilas ;j++){
            var probabilidad = Math.floor((Math.random() * 300) + 1);
            //Probabilidad de aparicion de montaña
            if(probabilidad <= 1 && mapa[j][i] =="prado"){
              //Aparece montaña
              mapa[j][i]="montana";

              //Encuentra el primer oceano 
              var xCentro ;
              var yCentro ; 
              var oceanoCercano;
              var distancia;
              for(t=0;t<5;t++){
                if(oceanoOcupado[t] == 1){
                  oceanoCercano = t;
                  var centroOceano = getCentroOceano(t,nroFilas,nroColumnas);
                  xCentro = centroOceano[0];
                  yCentro = centroOceano[1];
                  var distancia = calcularDistancia(i,j,xCentro,yCentro);                  
                }
              }
             
              //Encuentra el oceano mas cercano
              for(t=0;t<5;t++){
                //No sea el mismo oceano
                if(oceanoOcupado[t] == 1 && oceanoCercano!=t){                  
                  var centroOceano = getCentroOceano(t,nroFilas,nroColumnas);
                  var xCentroNuevo = centroOceano[0];
                  var yCentroNuevo = centroOceano[1];
                  var distanciaNueva = calcularDistancia(i,j,xCentroNuevo,yCentroNuevo);
                  if(distanciaNueva < distancia){
                    distancia= distanciaNueva;
                    oceanoCercano = t;
                    xCentro = xCentroNuevo;
                    yCentro = yCentroNuevo;
                  }
                }
              }              

              //Traza la ruta al oceano mas cercano
              var iAct = i;
              var jAct = j;
              while(iAct != xCentro && jAct != yCentro){
                    if(Math.abs(iAct-xCentro) >= Math.abs(jAct-yCentro)){
                       //Avanza en el eje x
                      //Determina si es derecha o izquierda
                      if(iAct-xCentro >= 0){
                         //Izquierda
                        iAct--;
                      }else{
                        //Derecha
                        iAct++;
                      }
                    }else{
                      //Avanza en el eje y
                      //Determina si es arriba o abajo
                      if(jAct-yCentro >= 0){
                         //Arriba
                        jAct--;
                      }else{
                        //Abajo
                        jAct++;
                      }                      
                    }
                //Establece la corriente del rio
                mapa[jAct][iAct] = "oceano";
              }
              
              nroRios++; 
            }
          }
        }        
      }
      
      //-----Asignar camino
      for(i=0; i<nroColumnas;i++){
        for(j=0 ; j<nroFilas ;j++){
          var probabilidad = Math.floor((Math.random() * 100) + 1);
          //Probabilidad de aparicion de camino
          if(probabilidad <= 2 ){
            var iAct = i;
            var jAct = j;
             //Comienza a dibujar un camino
            terminaCamino = false;
            while(!terminaCamino){
                  var sigueCamino = Math.floor((Math.random() * 100) + 1);
                  if(sigueCamino <= 50){
                    //Elige una dirección del camino
                    var direccion = Math.floor((Math.random() * 4) + 1);                    
                    var nroBaldosas = 18;
                    for(k=0;k<nroBaldosas;k++){
                      var nroCaminoFila= Math.floor((Math.random() * 2) + 0);
                      var nroCaminoColumna= Math.floor((Math.random() * 6) + 0);
                      
                      var puedeDibujar = true;
                      //Si arriba esta disponible
                      if(direccion == 1 && (jAct-1) >= 0){
                        jAct--;
                      }else if(direccion == 2 && (iAct+1) < nroColumnas){
                        iAct++;    
                      }else if(direccion == 3 && (jAct+1) < nroFilas){
                        jAct++;  
                      }else if(direccion == 4 && (iAct-1) >= 0){
                        iAct--;   
                      }else{
                        puedeDibujar = false;
                      }
                      
                      if(puedeDibujar && mapa[jAct][iAct] != "oceano" && mapa[jAct][iAct] != "montana"){
                        mapa[jAct][iAct] = "camino";
                      }
                    }

                  }else{
                    terminaCamino = true;
                  }
            }
          }
        }
      } 
      
      //---Pintar cuadros de la capa 1
      for(i=0; i<nroColumnas;i++){
        for(j=0 ; j<nroFilas ;j++){
          //Escoge baldosa
          var baldosa;
          var tipoBaldosa;
          //console.log("i:",i,"  j:",j,"  ",mapa[j][i]);
          if(mapa[j][i] == "prado"){ 
            tipoBaldosa = Math.floor((Math.random() * tilesPrado.n) + 0); 
            baldosa = tilesPrado[tipoBaldosa.toString()];                         
          }else if(mapa[j][i] == "oceano"){
            tipoBaldosa = Math.floor((Math.random() * tilesOceano.n) + 0);            
            baldosa = tilesOceano[tipoBaldosa.toString()];  
          }else if(mapa[j][i] == "rio"){
            tipoBaldosa = Math.floor((Math.random() * tilesOceano.n) + 0);            
            baldosa = tilesOceano[tipoBaldosa.toString()];                   
          }else if(mapa[j][i] == "camino"){
            tipoBaldosa = Math.floor((Math.random() * tilesCamino.n) + 0);  
            baldosa = tilesCamino[tipoBaldosa.toString()];                   
          }
          //Dibuja
          contexto1.drawImage(imageTile, baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);           
        }
      }
      
    }   
    
    var imageTree = new Image();
    imageTree.src = tilesBosque.path;
    imageTree.onload = function() {    
      //Dibujar bosque
      for(i=0;i<nroColumnas;i++){
        for(j=0 ; j<nroFilas ;j++){
          
             var probabilidad = Math.floor((Math.random() * 100) + 1);
            if(probabilidad <= 2){
              
              //Escoge el radio del bosque
              var radioBosque = Math.floor((Math.random() * ((nroJugadores/2))) + 1);
              
              //Escoge el tipo de bosque
              var tipoBosque = Math.floor((Math.random() * parseInt(tilesBosque.n)) + 0);               
              //Trasladamos para dibujar una circunferencia
              iIni = i-radioBosque;
              jIni = j-radioBosque;
              for(iAct = iIni; iAct < iIni + (radioBosque*2)+1;iAct++){
                for(jAct = jIni; jAct < jIni + (radioBosque*2)+1;jAct++){
                  
                  //Determinar si el punto pertenece al mapa
                  if(iAct>=0 && iAct< nroColumnas && jAct>=0 && jAct<nroFilas){
                    
                    //Determinar si el punto pertenece a la circunferencia
                    if(Math.pow(iAct-i,2)+Math.pow(jAct-j,2)<=Math.pow(radioBosque,2)){
                      
                      //No sobreescribir el bosque
                      if(mapa[jAct][iAct] != "bosque" && mapa[jAct][iAct] != "camino" && mapa[jAct][iAct] != "oceano" && mapa[jAct][iAct] != "montana"){
                         mapa[jAct][iAct] = "bosque";
                          tipoBosque = tipoBosque.toString();
                          var arbol = tilesBosque[tipoBosque];                      
                           contexto2.drawImage(imageTree, arbol["x0"], arbol["y0"], arbol["x1"]-arbol["x0"], arbol["y1"]-arbol["y0"], iAct*tamCol, jAct*tamFil,  tamCol, tamFil);                         
                           }                                            
                    }
                  }
                }
              }
                          
            }        
        }
      }   
    }
    
    
    //----montana
    var imageMontana = new Image();
    imageMontana.src = tilesMontana.path;
    imageMontana.onload = function() {
      for(i=0; i<nroColumnas;i++){
        for(j=0 ; j<nroFilas ;j++){
          //Escoge baldosa
          var baldosa;
          var tipoBaldosa;
        
          if(mapa[j][i] == "montana"){
            tipoBaldosa = Math.floor((Math.random() * tilesMontana.n) + 0);  
            console.log("x:",i,"  y:",j,"  tipoMontana:",tipoBaldosa);
            baldosa = tilesMontana[tipoBaldosa.toString()]; 
            contexto2.drawImage(imageTile, baldosa["x0"], baldosa["y0"], baldosa["x1"]-baldosa["x0"], baldosa["y1"]-baldosa["y0"], i*tamCol, j*tamFil, tamCol, tamFil);             
          }  
        }
      }
    }
}

function calcularDistancia(x0,y0,x1,y1){ 
  return Math.pow(x0-x1,2) + Math.pow(y0-y1,2);
}

function getCentroOceano(indice,nroFilas,nroColumnas){
var xCentro, yCentro;
  if(indice == 0){
     xCentro = 0;
     yCentro = 0;
  }else if(indice == 1){
     xCentro = nroColumnas-1;
     yCentro = 0;                 
  }else if(indice == 2){
     xCentro = nroColumnas-1;
     yCentro = nroFilas-1;                 
  }else if(indice == 3){
     xCentro = 0;
     yCentro = nroFilas-1;                 
  }else if(indice == 4){
     xCentro = Math.floor((nroColumnas-1)/2);
     yCentro = Math.floor((nroFilas-1)/2);                 
  }  
  return [xCentro, yCentro];
}