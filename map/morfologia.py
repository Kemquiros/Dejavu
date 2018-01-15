import numpy as np

def crearKernel(tamKernel):
  #Crear Kernel en cruz
  centroKernel = tamKernel/2
  kernel = np.zeros((tamKernel,tamKernel))
  for i in range(0,tamKernel):
    for j in range(0,tamKernel):
      if(i==centroKernel or j==centroKernel):
        kernel[i][j] = 1
      else:
        kernel[i][j] = 0
  return kernel, centroKernel

def createReferenceMap(nroFilas,nroColumnas):  
  #Creamos un nuevo mapa de refencia
  #El cual va a modificar al mapa real  
  return np.zeros((nroFilas,nroColumnas))

def erode(mapa, nroFilas,nroColumnas, tamKernel):
  #Crear Kernel
  kernel, centroKernel = createKernel(tamKernel)
  
  #Creamos un nuevo mapa de refencia
  #El cual va a modificar al mapa real  
  mapaReferencia = createReferenceMap(nroFilas,nroColumnas)
  
  #Se buscan los cuadros a erosionar
  for i in range(0,nroColumnas):
    for j in range(0,nroFilas):
      if(mapa[j][i]==2):
        puntosCoinciden = True
        for m in range(0,tamKernel):
          for n in range(0,tamKernel):
            iAct = i - centroKernel + m
            jAct = j - centroKernel + n
            #Si el punto existe
            if(iAct >= 0 and iAct < nroColumnas and jAct >= 0 and jAct < nroFilas):              
              #Coinciden los puntos
              if(kernel[n][m]==1 and mapa[jAct][iAct] != 2):
                puntosCoinciden = False
      #Si la plantilla no coincide
      if(not puntosCoinciden):
        mapaReferencia[j][i] = 1
        
  #Se erosionan los cuadros
  for i in range(0,nroColumnas):
    for j in range(0,nroFilas):  
      if(mapaReferencia[j][i]==1):
          mapa[j][i] = 1
          
  return mapa
  
def dilate(mapa, nroFilas,nroColumnas, tamKernel):
  #Crear Kernel
  kernel, centroKernel = createKernel(tamKernel)
  
  #Creamos un nuevo mapa de refencia
  #El cual va a modificar al mapa real  
  mapaReferencia = createReferenceMap(nroFilas,nroColumnas)
  
  #Se buscan los cuadros a dilatar
  for i in range(0,nroColumnas):
    for j in range(0,nroFilas):
      if(mapa[j][i]==2):
        puntosCoinciden = True
        for m in range(0,tamKernel):
          for n in range(0,tamKernel):
            iAct = i - centroKernel + m
            jAct = j - centroKernel + n
            #Si el punto existe
            if(iAct >= 0 and iAct < nroColumnas and jAct >= 0 and jAct < nroFilas):               
              #Si el punto esta en el kernel
              #Pero no en el mapa
              if(kernel[n][m]==1 and mapa[jAct][iAct] != 2):
                mapaReferencia[jAct][iAct] = 1
              
  #Se dilatan los cuadros
  for i in range(0,nroColumnas):
    for j in range(0,nroFilas):
      if(mapaReferencia[j][i]==1):
        mapa[j][i] = 2
        
  return mapa
  