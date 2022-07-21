# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:08:19 2021

@author: Julien
"""


import numpy as np
import matplotlib.pyplot as plt

tabA = np.array([50.1,58.1,58.4,59.4,64.2,64.9,65.4,67.8,68.1,73.3,74.7,74.9,75.1,75.4,76,76,76.6,76.7,77.6,81.3])
tabB = np.array([58, 61.8, 63.7, 64, 64.4, 64.9, 65.3, 65.8, 66.8, 66.9, 67.5, 67.5, 67.8, 68.5, 68.7, 69.1, 69.5, 70.4, 71.8, 72])
tabC = np.array([58.6,61.8,62.8,63,63.1,63.3,63.7,64.2,64.4,65.3,69.3,70.9,73.7,73.8,73.9,74.4,76.3,76.9,78.4,78.8])

i=0
def analyse(tab):
    print(tab.mean())
    print(tab[len(tab)//2])
    print(tab[len(tab)//4], tab[3*len(tab)//4])
    print(tab.std())
    print(tab.sum())
    global i
    plt.boxplot(tab, positions=[i])
    i+=1

analyse(tabA)
analyse(tabB)
analyse(tabC)