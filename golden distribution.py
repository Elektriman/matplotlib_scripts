# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 18:18:37 2020

@author: Julien
"""

"""
imports
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

"""
constants
"""
gr = np.pi*(3-np.sqrt(5))
N = 500
k = 5


"""
flat distribution
"""
P = []

for i in np.arange(N):
    P.append(np.sqrt(i)*np.array([np.cos(i*gr),np.sin(i*gr)]))
P=np.array(P)

# plt.scatter(P[:,0],P[:,1], marker='.', c='k')
# plt.axis('equal')
# plt.show()


"""
spherical distribution
"""

fig1 = plt.figure(figsize=(7,7))
ax1 = fig1.add_subplot(111, projection='3d')

P2 = np.zeros((N,3))

f = lambda x : np.sqrt(k-x**2)
H = np.linspace(-1,1,N)*k

for i in range(N):   
    r = f(abs(H[i]))
    x,y = r*np.cos(i*gr),r*np.sin(i*gr)
    P2[i] = [x, y, H[i]]

ax1.scatter(P2[:,0],P2[:,1],P2[:,2], c=P2[:,2])

plt.show()
    






































