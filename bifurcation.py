# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 15:20:35 2020

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1 - x)

n = 10000
r = np.linspace(2.5,4,n)
iterations = 1000
last = 100
x = 1e-5 * np.ones(n)

grey173 = [1-173/255,1-173/255,1-173/255]

fig, ax = plt.subplots(1, 1, figsize=(8, 9))

for i in range(iterations):
    x = logistic(r, x)
    if i >= (iterations - last):
        ax.plot(r, x, ',', c=grey173, alpha=.25)

ax.set_xlim(0, 4)
plt.title("Bifurcation diagram")
plt.xlabel('logistic sequence parameter')
plt.ylabel('limit value(s)')

ax.plot([0,1],[0,0], c='k')
r0 = np.linspace(1,2.99,1000)
l = lambda r : (r-1)/r
ax.plot(r0, l(r0), c=grey173)

plt.show()





















