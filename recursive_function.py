# Codez, testez et visualisez la méthode du point fixe

import numpy as np
import matplotlib.pyplot as plt

def l(x):
    return 1.5*x*(1 - x)

#fonction qui renvoie une troncature de nb à n chiffres après la virgule
def getDec(nb, n):
    s = str(nb)
    i=0
    while i<len(s) and s[i]!="." :
        i+=1
    i = min(len(s), i+n)
    return float(s[:i])

#méthode du point fixe de manière récursive
def pointFixeRec(f, x0, i=0):
    if i>1000 :
        print("la méthode a échoué")
        return None
    else :
        if f(x0)!=x0 :
            return pointFixe(f, f(x0), i+1)
        else :
            return x0

def pointFixe(f, x0, e):
    X=[x0, f(x0)]
    while len(X)<1000 and getDec(X[-2], e)!= getDec(X[-1], e) :
        X.append(f(X[-1]))
    return X

def afficherPF(f, x0, e):
    X = pointFixe(f,x0,e)
    print(X)
    XX = np.linspace(0,1,1000)
    YY = f(XX)
    plt.plot(XX,YY, c='C00')
    plt.plot(XX,XX, c='C01')
    plt.axvline(x=0, c='k')
    plt.axhline(y=0, c='k')
    plt.grid(True)
    
    for i in range(len(X)-2):
        plt.plot([X[i],X[i+1]],[X[i+1], X[i+1]], c='g')
        plt.plot([X[i+1],X[i+1]],[X[i+1],X[i+2]], c='g')
        plt.show()

afficherPF(l, 0.2, 10)