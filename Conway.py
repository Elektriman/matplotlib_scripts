# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:26:29 2021

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

np.random.seed(220920)
N = 50
U = np.full((N,N), False)

pattern =  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

U[0:9,0:39] = pattern

def voisins(case):
    x,y = case
    V = []
    A = [-1,0,1,-1,1,-1,0,1]
    B = [-1,-1,-1,0,0,1,1,1]
    for (i,j) in zip(A,B):
        if (i,j)!=(0,0) :
            a,b = (x+i)%N,(y+j)%N
            if U[a,b] :
                V.append((a,b))
    return V

def evolve(U):
    W = U.copy()
    for i in range(len(U)):
        for j in range(len(U[0])):
            V = voisins((i,j))
            if U[i,j] :
                if len(V)>3 or len(V)<2 :
                    W[i,j]=False
            else :
                if len(V)==3 :
                    W[i,j]=True
    return W

def generate_data() :
    global U
    U = evolve(U)
    return(U)

def update(data) :
    mat.set_data(data)
    return(mat)

def data_gen() :
    while True:
        yield generate_data()

fig, ax = plt.subplots()

mat = ax.matshow(generate_data())
ani = animation.FuncAnimation(fig, update, data_gen, interval=100)
plt.show()































