# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:34:47 2020

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0,3.5,1000)
sec = 0
while T[sec]<1 :
    sec+=1

dt = (T[-1]-T[0])/1000

hit = 0

X = np.full(1000,0.0)
X[0]=-58
V = np.full(1000,0.0)
V[0]=22
A = np.array([0.0]*sec + [-4.0]*(1000-sec))

for i in range(1,1000):
    if V[i]>=0 :
        V[i]=max(V[i-1]+A[i]*dt,0)
        X[i]=X[i-1]+V[i]*dt
    if X[i]<0 :
        hit=i

print(T[hit], V[hit])

fig,ax = plt.subplots(3,1,sharex=True)

ax[0].plot(T[:sec],X[:sec], c='C1')
ax[0].plot(T[sec:],X[sec:], label="position")
ax[0].plot([0,T[-1]],[0,0],c='grey', lw=1, zorder=-1)
ax[0].legend()

ax[1].plot(T[:sec],V[:sec], c='C1')
ax[1].plot(T[sec:],V[sec:], label="velocity")
ax[1].plot([0,T[-1]],[0,0],c='grey', lw=1, zorder=-1)
ax[1].legend()

ax[2].plot(T[:sec],A[:sec], c='C1')
ax[2].plot(T[sec:],A[sec:], label="acceleration")
ax[2].plot([0,T[-1]],[0,0],c='grey', lw=1, zorder=-1)
ax[2].legend()

plt.show()
