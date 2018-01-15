import numpy as np
import random
import math
from morfologia import dilate, erode

class Mapa:
  numeroCapas = 4
  promMovimiento = 7
  
  tamCol = 40
  tamFil = 40
  
  traslacionCapa = {1:"prado",2:"oceano",3:"rio",4:"camino",5:"bosque",6:"montana",7:"nieve",8:"pantano",9:"castillo",10:"aldea",11:"ciudad",12:"templo",13:"portal"}
  
  def __init__(self,numeroJugadores):
    self.nroJugadores = numeroJugadores
    self.nroFilas = self.nroJugadores * self.promMovimiento
    self.nroColumnas = self.nroJugadores * self.promMovimiento
    self.nroOceanosMax = (self.nroJugadores/4)+1
    self.nroRiosMax = (self.nroJugadores/2)+1
    self.mapa = np.zeros((self.nroFilas,self.nroColumnas))
    self.crearMapa()
    
  def crearMapa(self):
    self.crearPrado()
    self.crearOceano()
  
  def crearPrado(self):
    for i in range(0,self.nroFilas):
      for j in range(0,self.nroColumnas):
        self.mapa[i][j] = 1

  def getCentroOceano(indice,nroFilas,nroColumnas):
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
      xCentro = (nroColumnas-1)/2
      yCentro = (nroFilas-1)/2
    return xCentro,yCentro
  
  def calcularDistancia(x0,y0,x1,y1):
    return math.sqrt(math.pow(x0-x1,2) + math.pow(y0-y1,2))
  
  def gaussianPDF(mean, variance, x):
    standardDeviation = math.sqrt(variance)
    m = standardDeviation * math.sqrt(2 * math.pi)
    
    
  def crearOceano(self):    
    oceanoOcupado = np.zeros((5))
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
          puedeContinuar = true
      
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
            self.mapa[j][i] = 2
            
    #Aplicar factor morfologico closing
    #closing =  dilatacion -> erosion
    for i in range(0,3):
      #Dilatacion
      self.mapa = dilate(self.mapa, self.nroFilas,self.nroColumnas, 3)
      #Erosion
      self.mapa = erode(self.mapa, self.nroFilas,self.nroColumnas, 3)
    #Pule los bordes
    self.mapa = erode(self.mapa, self.nroFilas,self.nroColumnas, 3)
    
    