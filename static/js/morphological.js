function createKernel(tamKernel){
  //crear kernel
  var centroKernel = Math.floor(tamKernel/2);
  var kernel = new Array(tamKernel );
  for(i=0;i<tamKernel ;i++){
    kernel[i] = new Array(tamKernel );
    for(j=0;j<tamKernel ;j++){
      if(i==centroKernel||j==centroKernel){
         kernel[i][j] = 1;
      }else{
        kernel[i][j] = 0;
      }
    }
  }  
  return [kernel,centroKernel];
}

function createReferenceMap(nroFilas,nroColumnas){
  //Creamos un nuevo mapa de refencia
  //El cual va a modificar al mapa real
  var mapaReferencia = new Array(nroFilas);
  for(i=0; i<nroFilas; i++){
    mapaReferencia[i] = new Array(nroColumnas);
    for(j=0; j<nroColumnas; j++ ){
      mapaReferencia[i][j] = 0;
    }
  }    
  return mapaReferencia;
}

function erode(mapa, nroFilas,nroColumnas, tamKernel){
    //Crear kernel
    var resp = createKernel(tamKernel);
    var kernel = resp[0];
    var centroKernel = resp[1];
  
    //Creamos un nuevo mapa de refencia
    //El cual va a modificar al mapa real
    var mapaReferencia = createReferenceMap(nroFilas,nroColumnas);
  
    //Se buscan los cuadros a erosionar
    for(i=0; i<nroColumnas ;i++){
      for(j=0 ; j<nroFilas ;j++){
        if(mapa[j][i]=="oceano"){
          var puntosCoinciden = true;
          for(m=0; m < tamKernel ; m++ ){
            for(n=0; n < tamKernel ; n++){
              var iAct = i - centroKernel + m;
              var jAct = j - centroKernel + n;
              //Si el punto existe
              if(iAct >= 0 && iAct < nroColumnas && jAct >= 0 && jAct < nroFilas){
                 //Coinciden los puntos
                  if(kernel[n][m]==1 && mapa[jAct][iAct] != "oceano"){
                     puntosCoinciden = false;
                  }
              }
            }
          }
        }
        //Si la plantilla no coincide
        if(!puntosCoinciden){
           //Se indica el cuadro a erosionar
            mapaReferencia[j][i] = 1;
         }
      }
    }   
  
    //Se erosionan los cuadros
    for(i=0; i<nroColumnas ;i++){
      for(j=0 ; j<nroFilas ;j++){
        if(mapaReferencia[j][i]==1){
          mapa[j][i] = "prado";
        }
      }
    }  
  return mapa;
}

function dilate(mapa, nroFilas,nroColumnas, tamKernel){
    //Crear kernel
    var resp = createKernel(tamKernel);
    var kernel = resp[0];
    var centroKernel = resp[1];
  
    //Creamos un nuevo mapa de refencia
    //El cual va a modificar al mapa real
    var mapaReferencia = createReferenceMap(nroFilas,nroColumnas);
  
    //Se buscan los cuadros a dilatar
    for(i=0; i<nroColumnas ;i++){
      for(j=0 ; j<nroFilas ;j++){
        if(mapa[j][i]=="oceano"){
          for(m=0; m < tamKernel ; m++ ){
            for(n=0; n < tamKernel ; n++){
              var iAct = i - centroKernel + m;
              var jAct = j - centroKernel + n;
              //Si el punto existe
              if(iAct >= 0 && iAct < nroColumnas && jAct >= 0 && jAct < nroFilas){
                //Si el punto está en el kernel
                //Pero no en el mapa
                if(kernel[n][m]==1 && mapa[jAct][iAct] != "oceano"){
                   mapaReferencia[jAct][iAct] = 1;
                }
              }
            }
          }
        }
      }
    }
  
  //Se dilatan los cuadros
  for(i=0; i<nroColumnas ;i++){
    for(j=0 ; j<nroFilas ;j++){
      if(mapaReferencia[j][i]==1){
        mapa[j][i] = "oceano";
      }
    }
  }    
  
  return mapa;
}