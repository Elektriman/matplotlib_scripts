# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:32:47 2022

@author: Crambes
"""
import numpy as np
from scipy.special import gamma as Gamma
import matplotlib.pyplot as plt

def DL_sin(n):
    if n==0 :
        return lambda x : x
    else :
        return lambda x : DL_sin(n-1)(x) + ((-1)**n) * (x**(2*n+1))/Gamma(2*n+2)

X = np.linspace(0, 2*np.pi, 1000)
for i in range(7):
    plt.plot(X, DL_sin(i)(X), label=str(i))
plt.plot(X, np.sin(X), c='k', alpha = 0.2, zorder=-3)
plt.ylim(-1,1)
plt.legend()
plt.show()