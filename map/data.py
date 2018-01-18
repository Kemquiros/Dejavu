class DataMap():
  tamColumnas = 60
  tamFilas = 60
  promMovimiento = 7
  
  prado = {
    "path":"static/img/map/tiles1.png",
    "n" : 4,
    "0":{
      "x0":0,
      "y0":0,
      "x1":32,
      "y1":32
    },
    "1":{
      "x0":32,
      "y0":0,
      "x1":64,
      "y1":32
    },
    "2":{
      "x0":64,
      "y0":0,
      "x1":96,
      "y1":32
    },
    "3":{
      "x0":96,
      "y0":0,
      "x1":128,
      "y1":32
    },
    "4":{
      "x0":128,
      "y0":0,
      "x1":160,
      "y1":32
    },
    "5":{
      "x0":0,
      "y0":32,
      "x1":32,
      "y1":64
    }
  }
  
  oceano = {
    "path":"static/img/map/tiles1.png",
    "n" : 3,
    "0":{
      "x0":0,
      "y0":417,
      "x1":31,
      "y1":447
    },  
    "1":{
      "x0":32,
      "y0":417,
      "x1":63,
      "y1":447
    }, 
    "2":{
      "x0":64,
      "y0":417,
      "x1":95,
      "y1":447
    } 
  }  
  
  rio = oceano
  
  camino = {
    "path":"static/img/map/tiles1.png",
    "n" : 5,
    "0":{
      "x0":32,
      "y0":33,
      "x1":64,
      "y1":64
    },  
    "1":{
      "x0":64,
      "y0":33,
      "x1":96,
      "y1":64
    }, 
    "2":{
      "x0":96,
      "y0":33,
      "x1":128,
      "y1":64
    },
    "3":{
      "x0":128,
      "y0":33,
      "x1":160,
      "y1":64
    },
    "4":{
      "x0":128,
      "y0":64,
      "x1":159,
      "y1":95
    }      
  }
  
  bosque = {
    "path":"static/img/map/trees.png",
    "n" : 8,
    "0":{
      "x0":0,
      "y0":0,
      "x1":144,
      "y1":121
    },
    "1":{
      "x0":144,
      "y0":0,
      "x1":247,
      "y1":125
    },
    "2":{
      "x0":248,
      "y0":0,
      "x1":350,
      "y1":125
    },  
    "3":{
      "x0":221,
      "y0":137,
      "x1":385,
      "y1":331
    }, 
    "4":{
      "x0":583,
      "y0":148,
      "x1":724,
      "y1":333
    }, 
    "5":{
      "x0":449,
      "y0":352,
      "x1":600,
      "y1":550
    }, 
    "6":{
      "x0":224,
      "y0":432,
      "x1":312,
      "y1":547
    },
    "7":{
      "x0":756,
      "y0":373,
      "x1":837,
      "y1":550
    }    
  }
  
  montana = {
    "path":"static/img/map/mountain0.png",
    "n" : 3,
    "0":{
      "x0":295,
      "y0":736,
      "x1":697,
      "y1":979
    },  
    "1":{
      "x0":0,
      "y0":0,
      "x1":303,
      "y1":255
    }, 
    "2":{
      "x0":321,
      "y0":0,
      "x1":567,
      "y1":237
    }     
  } 
  
  nieve = {
    "path":"static/img/map/tiles1.png",
    "n" : 4,
    "0":{
      "x0":0,
      "y0":768,
      "x1":31,
      "y1":799
    },  
    "1":{
      "x0":0,
      "y0":800,
      "x1":31,
      "y1":831
    }, 
    "2":{
      "x0":128,
      "y0":800,
      "x1":159,
      "y1":831
    },
    "3":{
      "x0":160,
      "y0":768,
      "x1":191,
      "y1":799      
    }
  }
  
  ciudad = {
    "path":"static/img/map/tiles2.png",
    "n" : 4,
    "0":{
      "x0":129,
      "y0":161,
      "x1":178,
      "y1":209
    },  
    "1":{
      "x0":14,
      "y0":582,
      "x1":67,
      "y1":636
    }, 
    "2":{
      "x0":125,
      "y0":1441,
      "x1":164,
      "y1":1505
    },
    "3":{
      "x0":2,
      "y0":1035,
      "x1":58,
      "y1":1086
    }     
  }    
  
  montanaNieve = {
    "path":"static/img/map/mountain3.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":332,
      "y1":354
    }  
  }
  
  castillo = {
    "path":"static/img/map/castle0.png",
    "n" : 8,
    "0":{
      "x0":32,
      "y0":436,
      "x1":309,
      "y1":720
    },  
    "1":{
      "x0":363,
      "y0":453,
      "x1":599,
      "y1":676
    }, 
    "2":{
      "x0":582,
      "y0":146,
      "x1":863,
      "y1":395
    },
    "3":{
      "x0":925,
      "y0":118,
      "x1":1650,
      "y1":756
    },
    "4":{
      "x0":1794,
      "y0":134,
      "x1":2364,
      "y1":688
    },
    "5":{
      "x0":2394,
      "y0":30,
      "x1":3158,
      "y1":698
    },
    "6":{
      "x0":3136,
      "y0":21,
      "x1":3841,
      "y1":717
    },
    "7":{
      "x0":3866,
      "y0":1,
      "x1":4738,
      "y1":748
    }
  }      
  
  templo = {
    "path":"static/img/map/tiles2.png",
    "n" : 1,
    "0":{
      "x0":127,
      "y0":1348,
      "x1":192,
      "y1":1440
    }  
  }  
  
  taberna = {
    "path":"static/img/map/tavern0.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":483,
      "y1":455
    }  
  }  
  
  aldea = {
    "path":"static/img/map/village0.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":518,
      "y1":311
    }  
  }   
  
  montanaSagrada = {
    "path":"static/img/map/mountain1.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":272,
      "y1":163
    }  
  }   
  
  tiles = {
    1 : prado,
    2 : oceano,
    3 : rio,
    4 : camino,
    5 : bosque,
    6 : montana,
    7 : nieve, #nieve
    8 : taberna, #taberna
    9 : castillo, #castillo
    10 : aldea, #aldea
    11 : ciudad, #ciudad
    12 : templo, #templo
    13 : None, #portal
    14 : montanaNieve,
    15 : montanaSagrada
  }  
  
  vampiro = {
    "path":"static/img/tile/Vampiro.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":369,
      "y1":498
    }     
  }
  hombreLobo = {
    "path":"static/img/tile/Hombre_Lobo.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":982,
      "y1":1024
    }     
  } 
  
  demiurgo = {
    "path":"static/img/tile/selection/Demiurgo.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":450,
      "y1":600
    }     
  }  
  
  cazador = {
    "path":"static/img/tile/selection/Cazador.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":421,
      "y1":527
    }     
  }
  
  hechizero = {
    "path":"static/img/tile/selection/Hechizero.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":842,
      "y1":842
    }     
  }  
  
  nigromante = {
    "path":"static/img/tile/Nigromante.png",
    "n" : 1,
    "0":{
      "x0":0,
      "y0":0,
      "x1":900,
      "y1":1430
    }     
  }  
  
  avatar = {
    1 : vampiro,
    2 : hombreLobo,
    3 : demiurgo,
    4 : cazador,
    5 : hechizero,
    6 : nigromante
  }
