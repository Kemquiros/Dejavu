# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import random
import math
from morfologia import dilate, erode
from data import DataMap
from castillo import Castillo

class Mapa:
  
  data = DataMap()
  
  traslacionCapa = {1:"prado",2:"oceano",3:"rio",4:"camino",5:"bosque",6:"montana",7:"nieve",8:"pantano",9:"castillo",10:"aldea",11:"ciudad",12:"templo",13:"portal",14:"montana-nieve"}
  nroTile = {
    1:data.tiles[1]["n"],
    2:data.tiles[2]["n"],
    3:data.tiles[3]["n"],
    4:data.tiles[4]["n"],
    5:data.tiles[5]["n"],
    6:data.tiles[6]["n"],
    7:data.tiles[7]["n"],
    9:data.tiles[9]["n"],
    11:data.tiles[11]["n"],
    14:data.tiles[14]["n"]
  }
  
  def __init__(self,numeroJugadores):
    self.nroJugadores = numeroJugadores
    self.nroFilas = self.nroJugadores * self.data.promMovimiento
    self.nroColumnas = self.nroJugadores * self.data.promMovimiento
    self.nroOceanosMax = int(self.nroJugadores/4)+1
    self.nroRiosMax = int(self.nroJugadores/2)+1
    self.mapa1 = np.zeros((self.nroFilas,self.nroColumnas))
    self.mapa2 = np.zeros((self.nroFilas,self.nroColumnas))
    self.mapa3 = np.zeros((self.nroFilas,self.nroColumnas))
    self.visual1 = np.zeros((self.nroFilas,self.nroColumnas))
    self.visual2 = np.zeros((self.nroFilas,self.nroColumnas))
    self.castillos = {}
    self.crearMapa()
    
  def crearMapa(self):
    self.crearPrado() 
    self.crearOceano() 
    self.crearRio()#self.montanaNieve() 
    self.crearBosque()
    self.crearMontana()
    self.crearCiudad()#self.crearCamino()        
    self.crearCastillo()
    #self.crearTemplo()
    
    
    
  
  def crearPrado(self):
    for i in range(0,self.nroFilas):
      for j in range(0,self.nroColumnas):
        self.mapa1[i][j] = 1     
        self.visual1[i][j] = random.randint(1,self.nroTile[1]) -1

  def getCentroOceano(self,indice,nroFilas,nroColumnas):
    xCentro = -1
    yCentro = -1
    if(indice == 0):
      xCentro = 0
      yCentro = 0
    elif(indice == 1):
      xCentro = int(round((nroColumnas-1)/2))
      yCentro = 0
    elif(indice == 2):
      xCentro = nroColumnas-1
      yCentro = 0
    elif(indice == 3):
      xCentro = nroColumnas-1
      yCentro = int(round((nroFilas-1)/2))
    elif(indice == 4):
      xCentro = nroColumnas-1
      yCentro = nroFilas-1  
    elif(indice == 5):
      xCentro = int(round((nroColumnas-1)/2))
      yCentro = nroFilas-1
    elif(indice == 6):
      xCentro = 0
      yCentro = nroFilas-1 
    elif(indice == 7):
      xCentro = 0
      yCentro = int(round((nroFilas-1)/2))     
    elif(indice == 8):
      xCentro = int(round((nroColumnas-1)/2))
      yCentro = int(round((nroFilas-1)/2))
    elif(indice == 9):
      xCentro = int(round((nroColumnas-1)/4))
      yCentro = int(round((nroFilas-1)/4))
    elif(indice == 10):
      xCentro = int(round(3*(nroColumnas-1)/4))
      yCentro = int(round((nroFilas-1)/4))    
    elif(indice == 11):
      xCentro = int(round(3*(nroColumnas-1)/4))
      yCentro = int(round(3*(nroFilas-1)/4)) 
    elif(indice == 12):
      xCentro = int(round((nroColumnas-1)/4))
      yCentro = int(round(3*(nroFilas-1)/4))      
    return xCentro,yCentro
  
  def calcularDistancia(self,x0,y0,x1,y1):
    return math.sqrt(math.pow(x0-x1,2) + math.pow(y0-y1,2))
  
  def gaussianPDF(self,mean, variance, x):
    standardDeviation = math.sqrt(variance)
    m = standardDeviation * math.sqrt(2 * math.pi)
    e = math.exp(-1*math.pow(x -mean, 2) / (2 * variance))
    return e / m
    
    
  def crearOceano(self):    
    self.oceanoOcupado = np.zeros((13))
    for nroOceanos in range(0,self.nroOceanosMax):
      tamOceano = (self.data.promMovimiento) * random.randint(1, self.nroJugadores)
      
      #Selecciona un oceano libre
      puedeContinuar = False
      oceano = -1
      while(not puedeContinuar):
        #Selecciona uno de los 13 oceanos
        oceano = random.randint(0, 12)
        if(self.oceanoOcupado[oceano]==0):
          self.oceanoOcupado[oceano] = 1
          puedeContinuar = True
      
      '''
          ---------
         |0   1   2|
         |  9   10 |
         |7   8   3|
         |  12  11 |
         |6   5   4|
          ---------
      '''
      xCentro,yCentro = self.getCentroOceano(oceano,self.nroFilas,self.nroColumnas)
      
      #Recorre todo el mapa y dibuja el oceano
      #Segun la distancia entre la casilla y el centro del oceano
      for i in range(0,self.nroFilas):
        for j in range(0,self.nroColumnas):
          distancia = self.calcularDistancia(i,j,xCentro,yCentro)
          probabilidad = self.gaussianPDF(0, tamOceano, distancia)
          if( random.random() <= (probabilidad*12) ):
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
    #Asignar componenete visual
    for i in range(0,self.nroFilas):
      for j in range(0,self.nroColumnas):
        if self.mapa1[j][i] == 2:
          self.visual1[j][i] = random.randint(1,self.nroTile[2]) -1
    
  def crearRio(self):
    for nroRios in range(0,self.nroRiosMax):
      for i in range(0,self.nroColumnas):
        for j in range(0,self.nroFilas):
          probabilidad = random.randint(1, 500*int(self.nroJugadores/4))
          if(probabilidad <=1 and self.mapa1[j][i] == 1):
            #Aparece montana nieve
            iMontana = i
            jMontana = j
            
            #Encuentra el primer oceano ocupado
            xCentro,yCentro,oceanoCercano,distancia = None,None,None,None            
            for t in range(0,12):
              if(self.oceanoOcupado[t] == 1):
                oceanoCercano = t
                xCentro,yCentro = self.getCentroOceano(t,self.nroFilas,self.nroColumnas)
                distancia = self.calcularDistancia(i,j,xCentro,yCentro)
                break
                
            #Encuentra el oceano mas cercano
            for t in range(0,12):
              #No sea el mismo oceano
              if(self.oceanoOcupado[t] == 1 and oceanoCercano!=t):
                xCentroNuevo,yCentroNuevo = self.getCentroOceano(t,self.nroFilas,self.nroColumnas)
                distanciaNueva = self.calcularDistancia(i,j,xCentroNuevo,yCentroNuevo)
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
              if(math.fabs(iAct-xCentro) >= math.fabs(jAct-yCentro)):
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
                   
              #Erosiona montañas a su paso
              if self.mapa2[jAct][iAct] == 14:
                self.mapa2[jAct][iAct] = 0
              #Establece la corriente del rio
              self.mapa1[jAct][iAct] = 3
              self.visual1[jAct][iAct] = random.randint(1,self.nroTile[3]) -1
            #Genera nevado
            self.crearMontanaNieve(iMontana,jMontana)

  def puntoPerteneceMapa(self,x,y):
    if(x>=0 and x< self.nroColumnas and y>=0 and y<self.nroFilas):
      return True
    return False
  
  def puntoPerteneceCircunferencia(self,x,y,xCentro,yCentro,r):
    if(math.pow(x-xCentro,2) + math.pow(y-yCentro,2) <= math.pow(r,2)):
      return True
    return False
    
  def crearMontanaNieve(self,iM,jM):    
    self.mapa1[jM][iM] = 7 #nieve
    self.visual1[jM][iM] = random.randint(1,self.nroTile[7]) -1
    self.mapa2[jM][iM] = 14#montana-nieve
    self.visual2[jM][iM] = random.randint(1,self.nroTile[14]) -1
    
    #Establecer radio del nevado
    radio = random.randint(1,int(self.nroJugadores/3))
    iIni = iM - radio
    jIni = jM - radio
    for i in range(iIni,iIni+(radio*2)+1):
      for j in range(jIni,jIni+(radio*2)+1):
        #Determinar si el punto pertenece al mapa
        if(self.puntoPerteneceMapa(i,j)):
          #Determinar si el punto pertenece a la circunferencia
          if(self.puntoPerteneceCircunferencia(i,j,iM,jM,radio)):
            #No sobreescribir el rio o el oceano
            if(self.mapa1[j][i] == 1):
              self.mapa1[j][i] = 7 #Nieve
              self.visual1[j][i] = random.randint(1,self.nroTile[7]) -1              
            
  def crearBosque(self):
    for i in range(0,self.nroColumnas):
      for j in range(0,self.nroFilas):
        probabilidad = random.randint(1,200*int(self.nroJugadores/4))
        if(probabilidad <= 3 ):        
          #Establecer radio del bosque
          radio = random.randint(1,int(self.nroJugadores/2))
          iIni = i - radio
          jIni = j - radio
          tipoBosque = random.randint(1,self.nroTile[5]) -1
          for iAct in range(iIni,iIni+(radio*2)+1):
            for jAct in range(jIni,jIni+(radio*2)+1):
              #Determinar si el punto pertenece al mapa
              if(self.puntoPerteneceMapa(iAct,jAct)):
                #Determinar si el punto pertenece a la circunferencia
                if(self.puntoPerteneceCircunferencia(iAct,jAct,i,j,radio)):                
                  #Se puede establecer en prado o nieve sin montana
                  if(self.mapa1[jAct][iAct] == 1 or (self.mapa1[jAct][iAct] == 7 and self.mapa2[jAct][iAct] != 14) ):
                    #Si no hay arbol
                    #O si hay arbol, una baja probabilidad de ganarle
                    if(self.mapa2[jAct][iAct] != 5 or (self.mapa2[jAct][iAct] == 5 and random.randint(1,100)<=2)):
                      self.mapa2[jAct][iAct] = 5 #bosque
                      self.visual2[jAct][iAct] = tipoBosque
          
  def crearMontana(self):
    for i in range(0,self.nroColumnas):
        for j in range(0,self.nroFilas):
          probabilidad = random.randint(1,200)
          if(probabilidad <= 1 ):
            longitudCamino = random.randint(1,10)
            iAct = i
            jAct = j
            #Comienza a dibujar un camino
            terminaCamino = False
            while(not terminaCamino):
              sigueCamino = random.randint(1,100)
              if(sigueCamino <= 50):
                #Elige una direccion del camino
                direccion = random.randint(1,4)
                for k in range(0,longitudCamino):
                  puedeDibujar = True
                  if direccion == 1 and (jAct-1) >= 0:
                    jAct -=1
                  elif direccion == 2 and (iAct+1) < self.nroColumnas:
                    iAct +=1
                  elif direccion == 3 and (jAct+1) < self.nroColumnas:
                    jAct +=1
                  elif direccion == 4 and (iAct-1) < self.nroColumnas:
                    iAct -=1
                  else:
                    puedeDibujar = False
                  
                  if puedeDibujar and self.puntoPerteneceMapa(iAct,jAct):
                    #Si es prado o nieve                
                    if self.mapa1[jAct][iAct] == 1 or self.mapa1[jAct][iAct] == 7:
                      #Si no es una montana nevada
                      if self.mapa2[jAct][iAct] != 14:
                        self.mapa2[jAct][iAct] = 6
                        self.visual2[jAct][iAct] = random.randint(1,self.nroTile[6]) -1
              else:
                terminaCamino = True                          
                        
  def crearCiudad(self):
    for i in range(0,self.nroColumnas):
        for j in range(0,self.nroFilas):
          probabilidad = random.randint(1,600*int(self.nroJugadores/4))
          if(probabilidad <= 4 and (self.mapa1[j][i] == 1 or self.mapa1[j][i] == 7)):    
            #Establecer radio de la ciudad
            radio = random.randint(1,round(self.nroJugadores/3))
            iIni = i - radio
            jIni = j - radio
            tipoCiudad = random.randint(1,self.nroTile[11]) -1
            for iAct in range(iIni,iIni+(radio*2)+1):
              for jAct in range(jIni,jIni+(radio*2)+1):
                #Determinar si el punto pertenece al mapa
                if(self.puntoPerteneceMapa(iAct,jAct)):
                  probabilidadAparicion = random.randint(1,100)
                  if(probabilidadAparicion>10):
                    #Mapa1: Prado o nieve
                    #Mapa2: Si no hay nada
                    if self.mapa1[jAct][iAct] == 1 or self.mapa1[jAct][iAct] == 7:
                      if self.mapa2[jAct][iAct] == 0:
                        self.mapa2[jAct][iAct] = 11
                        self.visual2[jAct][iAct] = tipoCiudad
            #Crea un nuevo camino
            nroIntentosCamino = 0
            while(nroIntentosCamino <= 5):
              direccionCamino = random.randint(1,4)
              iNuevo,jNuevo = self.getPunto(i,j,direccionCamino)
              #El nuevo punto pertenece al mapa y es prado
              if(self.puntoPerteneceMapa(iNuevo,jNuevo) and self.mapa1[jNuevo][iNuevo] == 1):
                self.crearCamino(iNuevo,jNuevo)
                break
              else:
                nroIntentosCamino += 1
            
  def getPunto(self,i,j,direccion):
    if(direccion == 1):
      j -= 1 #arriba
    elif(direccion == 2):
      i +=1 #derecha
    elif(direccion == 3):
      j +=1 #abajo
    elif(direccion == 4):
      i -=1 #Izquierda    
    return i,j
  
  def direccionOpuesta(self,direccion):    
    if(direccion == 1): #arriba
      return 3 
    elif(direccion == 2):#derecha
      return 4
    elif(direccion == 3):#abajo
      return 1
    elif(direccion == 4):#Izquierda 
      return 2
    return None
 
                    
  def crearCamino(self,i,j): 
    direccion = random.randint(1,4)
    longitudCamino = random.randint(10,30)    
    for k in range(1,longitudCamino):
      if(direccion == 1):
        j -= 1 #arriba
      elif(direccion == 2):
        i +=1 #derecha
      elif(direccion == 3):
        j +=1 #abajo
      elif(direccion == 4):
        i -=1 #Izquierda 
      if(self.puntoPerteneceMapa(i,j)):
        #Si es prado con una casa o nada encima
        if(self.mapa1[j][i] == 1 and (self.mapa2[j][i] == 0 or self.mapa2[j][i] == 11 ) ):
          self.mapa1[j][i] = 4        
          self.visual1[j][i] = random.randint(1,self.nroTile[4]) -1
        else:
          direccion = random.randint(1,4)
      else:#Termina
        return None
    #Retoma la posibilidad de continuar el camino
    if(random.randint(1,100)<=80):
      self.crearCamino(i,j)
      
  def crearCastillo(self):
    nroMaxCastillos = self.nroJugadores * 2    
    while(len(self.castillos) < nroMaxCastillos):
      for i in range(0,self.nroColumnas):
          for j in range(0,self.nroFilas):
            probabilidad = random.randint(1,900*int(self.nroJugadores/4))
            if( probabilidad <= 2 ): 
              #Prado o nieve
              if( self.mapa1[j][i] == 1 or self.mapa1[j][i] == 7 ):
                #No contiene nada o es un arbol
                if( self.mapa2[j][i] == 0 or self.mapa2[j][i] == 5 ):
                  self.mapa2[j][i] = 9
                  self.visual2[j][i] = random.randint(1,self.nroTile[9]) -1
                  self.castillos[len(self.castillos)] = Castillo(j,i)