# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:58:24 2021

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

X = np.linspace(0, 2*np.pi, 1000)
DIFF = np.cos(X)-np.sin(X)

fig,ax = plt.subplots()

def animate(i):
    global DIFF
    
    ax.clear()
    plt.ylim(-1.1,1.1)
    ax.plot(X, np.sin(X)+(0.01*(i%100)*DIFF))

ani = animation.FuncAnimation(fig, animate, interval = 100)