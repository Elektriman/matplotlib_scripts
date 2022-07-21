# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:05:55 2021

@author: Julien
"""

import numpy as np
import matplotlib.pyplot as plt

def R(n, fig):
    if n==1 :
        return fig
    else :
        r = R(n-1, fig)
        a,b = r.shape
        res = np.full((a*fig.shape[0],b*fig.shape[1]), False)
        for i in range(fig.shape[0]):
            for j in range(fig.shape[1]):
                if fig[i,j] :
                    res[i*a:(i+1)*a,j*b:(j+1)*b] = r
                else :
                    res[i*a:(i+1)*a,j*b:(j+1)*b] = np.full((a,b), False)
        return res

clara ="""
00100
01010
01010
01010
11111
"""[1:-1]

H0 = np.array([[1,1,1],[1,0,1],[1,1,1]], dtype=bool)



H0 = np.array([list(map(int,c)) for c in clara.split("\n")], dtype=bool)
print(H0)
plt.imshow(R(5,H0), cmap='gray')