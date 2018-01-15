from __future__ import division
import numpy as np
import random
import math
from morfologia import dilate, erode

class Mapa:
  numeroCapas = 4
  promMovimiento = 7
  
  tamCol = 40
  tamFil = 40
  
  traslacionCapa = {1:"prado",2:"oceano",3:"rio",4:"camino",5:"bosque",6:"montana",7:"nieve",8:"pantano",9:"castillo",10:"aldea",11:"ciudad",12:"templo",13:"portal",14:"montana-nieve"}
  
  def __init__(self,numeroJugadores):
    self.nroJugadores = numeroJugadores
    self.nroFilas = self.nroJugadores * self.promMovimiento
    self.nroColumnas = self.nroJugadores * self.promMovimiento
    self.nroOceanosMax = int(self.nroJugadores/4)+1
    self.nroRiosMax = int(self.nroJugadores/2)+1
    self.mapa1 = np.zeros((self.nroFilas,self.nroColumnas))
    self.mapa2 = np.zeros((self.nroFilas,self.nroColumnas))
    self.mapa3 = np.zeros((self.nroFilas,self.nroColumnas))
    self.crearMapa()
    
  def crearMapa(self):
    self.crearPrado()
    self.crearOceano()
    self.crearRio()
  
  def crearPrado(self):
    for i in range(0,self.nroFilas):
      for j in range(0,self.nroColumnas):
        self.mapa1[i][j] = 1                                      

  def getCentroOceano(self,indice,nroFilas,nroColumnas):
    xCentro = -1
    yCentro = -1
    if(indice == 0):
      xCentro = 0
      yCentro = 0
    elif(indice == 1):
      xCentro = nroColumnas-1
      yCentro = 0
    elif(indice == 2):
      xCentro = nroColumnas-1
      yCentro = nroFilas-1   
    elif(indice == 3):
      xCentro = 0
      yCentro = nroFilas-1  
    elif(indice == 4):
      xCentro = int(round((nroColumnas-1)/2))
      yCentro = int(round((nroFilas-1)/2))
    return xCentro,yCentro
  
  def calcularDistancia(self,x0,y0,x1,y1):
    return math.sqrt(math.pow(x0-x1,2) + math.pow(y0-y1,2))
  
  def gaussianPDF(self,mean, variance, x):
    standardDeviation = math.sqrt(variance)
    m = standardDeviation * math.sqrt(2 * math.pi)
    e = math.exp(-1*math.pow(x -mean, 2) / (2 * variance))
    return e / m
    
    
  def crearOceano(self):    
    self.oceanoOcupado = np.zeros((5))
    for nroOceanos in range(0,self.nroOceanosMax):
      tamOceano = (self.promMovimiento/2) * random.randint(1, self.nroJugadores)
      
      #Selecciona un oceano libre
      puedeContinuar = False
      oceano = -1
      while(not puedeContinuar):
        #Selecciona uno de los 5 oceanos
        oceano = random.randint(0, 4)
        if(oceanoOcupado[oceano]==0):
          oceanoOcupado[oceano] = 1
          puedeContinuar = True
      
      '''
          -------
         |0     1|
         |   4   |
         |3     2|
          -------
      '''
      xCentro,yCentro = self.getCentroOceano(oceano,self.nroFilas,self.nroColumnas)
      
      #Recorre todo el mapa y dibuja el oceano
      #Segun la distancia entre la casilla y el centro del oceano
      for i in range(0,self.nroFilas):
        for j in range(0,self.nroColumnas):
          distancia = self.calcularDistancia(i,j,xCentro,yCentro)
          probabilidad = self.gaussianPDF(0, tamOceano, distancia)
          if( random.random() <= (probabilidad*10) ):
            self.mapa1[j][i] = 2
            
    #Aplicar factor morfologico closing
    #closing =  dilatacion -> erosion
    for i in range(0,3):
      #Dilatacion
      self.mapa1 = dilate(self.mapa1, self.nroFilas,self.nroColumnas, 3)
      #Erosion
      self.mapa1 = erode(self.mapa1, self.nroFilas,self.nroColumnas, 3)
    #Pule los bordes
    self.mapa1 = erode(self.mapa1, self.nroFilas,self.nroColumnas, 3)
    
  def crearRio():
    for nroRios in range(0,self.nroRiosMax):
      for i in range(0,self.nroColumnas):
        for j in range(0,self.nroFilas):
          probabilidad = random.randint(1, 300)
          if(probabilidad <=1 and self.mapa1[j][i] == 1):
            #Aparece montana nieve
            iMontana = i
            jMontana = j
            
            #Encuentra el primer oceano ocupado
            xCentro,yCentro,oceanoCercano,distancia = None,None,None,None            
            for t in range(0,5):
              if(self.oceanoOcupado[t] == 1):
                oceanoCercano = t
                xCentro,yCentro = getCentroOceano(t,nroFilas,nroColumnas)
                distancia = calcularDistancia(i,j,xCentro,yCentro)
                break
                
            #Encuentra el oceano mas cercano
            for t in range(0,5):
              #No sea el mismo oceano
              if(self.oceanoOcupado[t] == 1 and oceanoCercano!=t):
                xCentroNuevo,yCentroNuevo = getCentroOceano(t,nroFilas,nroColumnas)
                distanciaNueva = calcularDistancia(i,j,xCentroNuevo,yCentroNuevo)
                if(distanciaNueva < distancia):
                  distancia= distanciaNueva
                  oceanoCercano = t
                  xCentro = xCentroNuevo
                  yCentro = yCentroNuevo  
                  
            #Traza la ruta al oceano mas cercano
            iAct = i
            jAct = j
            while(iAct != xCentro and jAct != yCentro):
              #Busca el centro del oceano
              if(Math.abs(iAct-xCentro) >= Math.abs(jAct-yCentro)):
                #Avanza en el eje x
                #Detetrmina si es derecha o izquierda
                if(iAct-xCentro >= 0):
                  #Izquierda
                  iAct = iAct - 1
                else:
                   #Derecha
                   iAct = iAct + 1
              else:
                #Avanza en el eje y
                #Detetrmina si es arriba o abajo
                if(jAct-yCentro >= 0):
                  #Izquierda
                  jAct = jAct - 1
                else:
                   #Derecha
                   jAct = jAct + 1
                   
              #Establece la corriente del rio
              self.mapa1[jAct][iAct] = 3
            #Genera nevado
            self.crearMontanaNieve(iMontana,jMontana)
  def puntoPerteneceMapa(x,y):
    if(x>=0 and x< self.nroColumnas and y>=0 and y<self.nroFilas):
      return True
    return False
  
  def puntoPerteneceCircunferencia(x,y,xCentro,yCentro,r):
    if(math.pow(x-xCentro,2) + math.pow(y-yCentro,2) <= math.pow(r,2)):
      return True
    return False
    
  def crearMontanaNieve(iM,jM):    
    self.mapa1[jMontana][iMontana] = 7 #nieve
    self.mapa2[jMontana][iMontana] = 14#montana-nieve
    #Establecer radio del nevado
    radio = random.randint(1,int(self.nroJugadores/2))
    iIni = iM - radio
    jIni = jM - radio
    for i in range(iIni,iIni+(radio*2)+1):
      for j in range(jIni,jIni+(radio*2)+1):
        #Determinar si el punto pertenece al mapa
        if(selfpuntoPerteneceMapa(i,j)):
          #Determinar si el punto pertenece a la circunferencia
          if(puntoPerteneceCircunferencia(i,j,iM,jM,radio)):
            #No sobreescribir el rio o el oceano
            if(self.mapa1[jAct][iAct] != 3 and self.mapa1[jAct][iAct] != 2):
              self.mapa1[jAct][iAct] = 7 #Nieve
        