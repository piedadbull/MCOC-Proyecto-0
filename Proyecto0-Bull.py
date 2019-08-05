# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 20:03:13 2019

@author: piedi
"""

import numpy as sp
from matplotlib import pyplot
import math

h= 1
VolumenParaf32=[]
VolumenParaf64=[] 
errores=[] 

Radios=[1,2,3,4,5,6,7,8,9]

for R in Radios: 
    #VolumenParaf32
    Volumen1 =(math.pi*(R**2)*h)/3
    v1=sp.float32(Volumen1)
    VolumenParaf32.append(v1)
    
    #VolumenParaf64
    Volumen2 = (math.pi*(R**2)*h)/3
    v2=sp.float64(Volumen2)
    VolumenParaf64.append(v2)
    
    print 'Volumen para f32:',VolumenParaf32[-1],';',   'Volumen para f64:',VolumenParaf64[-1]      
 
    error= (abs(VolumenParaf64[-1]-VolumenParaf32[-1]))/VolumenParaf32[-1]
    errores.append(error)
    print 'Error:', errores[-1]
    
pyplot.plot(Radios,errores)
pyplot.ylabel("Error Relativo")
pyplot.xlabel("Radio")
