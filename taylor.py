# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:05:21 2020

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def fact(n):
    if n==0 :
        return 1
    else :
        return n*fact(n-1)

def DL(f,a,n):
    return lambda x : (-1)**n * ((x-a)**(2*n+1))/fact(2*n+1)


f = lambda x : np.sin(x)
X = np.linspace(-1,7,1000)
N = 12
P = []
a=0
for i in range(N):
    P.append(DL(f,a,i))

fig, ax = plt.subplots(1,1)


def animate(i):
    
    global N
    global f
    global P
    global X
    
    n = i%N
    
    poly = lambda x : np.sum(np.array([p(x) for p in P[:n]]))
    Y = np.zeros(X.shape)
    for j in range(len(X)):
        Y[j]=poly(X[j])
    
    ax.clear()
    ax.plot(X,f(X), alpha=0.5, label='sin(x)')
    ax.plot(X,Y, zorder = 3, label=f'DL en {a} à l\'ordre {n}')
    ax.set_xlim(-1,7)
    ax.set_ylim(-2,2)
    plt.grid(True)
    plt.axhline(0, c='k')
    plt.axvline(0, c='k')
    plt.legend(loc=1)

ani = animation.FuncAnimation(fig, animate, interval=1000)