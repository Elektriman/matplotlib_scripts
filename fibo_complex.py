# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 21:04:47 2020

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt
import math

GR = complex((1+np.sqrt(5))/2,0)
GR2 = complex((1-np.sqrt(5))/2,0)

def fibo(n):
    L=[0,1]
    while len(L)<n+1 :
        L.append(L[-2]+L[-1])
    return L

binet = lambda x : (GR**x + (GR2)**x)

X = np.linspace(0, 7 ,1000)
Y = binet(X)

plt.plot(Y[:].real , Y[:].imag)
plt.grid()
plt.axvline(x=0, c='k')
plt.axhline(y=0, c='k')
plt.show()