# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:12:46 2021

@author: 
Classe:
    
"""
#Remarquons qu'il manque un mot dans l'énoncé, le mot "voisines", 
#Ceci serait la vraie rectification de l'énoncé : 
#règle de de mort : si à l'instant t une case contenant une cellule vivante a exactement deux ou trois cellules voisines 
#contenant chacune une cellule vivante, alors elle contient encore une cellule vivante à l'instant t+1. 
#Dans le cas contraire la cellule meurt et la case se vide.
#Donc une case contient une cellule, qui est soit vivante, soit morte 
#Explications plus précises et rigoureuses de l'importance du mot voisines: 
#Reprenons la phrase de l'énoncé "si a l'instant t une case contient une cellule vivante qui a exactement deux ou trois cellules vivantes ... etc ",
#si on garde l'énoncé tel quel, on peut comprendre qu'une case est composée de plusieurs cases qui elles memes peuvent du coup contenir plusieurs cases, ainsi a l'infini

#Exercice 1

# Modules et fonctions importés
###############################
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Constantes et paramètres
##########################

# Fonctions
###########

#Exercice 2

def suite_u(n) :
    """
    Entrée: un nombre int
    Sortie: un couple u_0, liste
    """
    un_0 = 42
    liste = [42]
    for i in range(n) :
        un_0 = (16383*un_0) % 59047 #on met des espaces entre chaque comparateur afin d'améliorer la lisibilité pour le correcteur
        liste.append(un_0)
    return un_0, liste
## Test et Exo 1

# print(suite_u(995)[-1])
# print(suite_u(9997)[-1])
#on a u_995 vaut 20313
#○n a u_9997 vaut 2531
#ces valeurs sont obtenus en enlevant le "un0," dans le return de la ligne 38
#print(suite_u(12))

#Exercice 3

un_0 = 42
compteur = 0
compteur2 = 0

liste = suite_u(10000)[1]
for i in range(0,10000):
    if liste[i] % 3 == 0:
        compteur += 1
    else:
        compteur2 += 1
# print("nombres divisibles par 3:", compteur, "pas divisible par 3:", compteur2)
#nombres divisibles par 3: 3307 pas divisible par 3: 6693

#Exercice 4

def genere_univers(k) :
    """Entree: int element k
        Sortie: renvoie le tableau a 
    """
    a = np.zeros(shape = (k, k)) 
    u = suite_u(k*k)[1]
    for i in range(k):
        for j in range(k):
            if u[i+j*k]% 3 == 0:
                a[i,j] = 1
    return a
# print(genere_univers(20))
## Test

# T = genere_univers(50)
# vivant = 0
# for i in range(50):
#     for j in range(50):
#         vivant = vivant + T[i][j]
# print(vivant) 
# print(genere_univers(20))
# print(sum(sum(genere_univers(20))))
# print(sum(sum(genere_univers(50))))
#pour k=20 on a 128 cellules vivantes
#pour k=50 on a 815 cellules vivantes

#Exercice 5

#Q1
def evolue(A) :
    """
    Entrée : un tableau qu'on donne en argument appelant la fonction
    Description: on visite chaque case i,j du tableau A donné en entrée et on compte son nombre de voisins vivants qu'on stocke dans la variable NbdeVivant
    Sortie : 
        tableau à l'instant t+1
    """
    n = len(A)
    N = np.zeros( shape = (n, n))
    if (n>2) :
      for i in range(n) :
        for j in range(n) :
            nbDeVivant = A[(i+1) % n][j] + A[(i-1) % n][j] + A[i][(j-1) % n] + A[i][(j+1) % n] + A[(i-1) % n][(j-1) % n] + A[(i-1) % n][(j+1) % n] + A[(i+1) % n][(j-1) % n] + A[(i+1) % n][(j+1) % n]
            if (A[i][j] == 1) : #si la cellule est vivante
                if (nbDeVivant == 2 or nbDeVivant == 3) : #si elle a 2 ou 3 voisins vivants
                    N[i][j] = 1 #alors elle reste vivante
                else :
                    N[i][j] = 0 #elle meurt
            else : #cas où la case contient une cellule morte
                if (nbDeVivant == 3) : #si elle a 3 voisines vivantes
                    N[i][j] = 1 #elle devient vivante 
                else :
                    N[i][j] = 0 #elle meurt
    else :
      if (2 <= A[0][0] + A[0][1] + A[1][0] + A[1][1] <= 3) :
        N[0][0] ,N[0][1], N[1][0], N[1][1] = 1, 1, 1, 1
    return N
    
# Test
#print(evolue([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1]]))
#print(evolue([[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,1,1]]))
#print(evolue([[0,0,0,0],[0,1,1,0],[0,1,0,0],[0,0,0,0]]))
#print(evolue([[1,1],[0,1]]))
#en testant et après de longues heures de dur labeur on remarque que c'est bon
#n est la taille du tableau
#quand n=2 le tableau est de la forme:
#[a,b]
#[c,d]
#toutes les cellules ont 3 voisins
#dès que la taille du tableau n est supérieur ou egale a 3. tous les cellules ont exactement 8 voisins
#ici, il y a un piège à éviter. En effet, si on modifie le tableau de l'étape k pour fabriquer celui de l'étape k+1, on laisse des modificationsde l'étape k avoir un rôle dans l'évolution à l'étape k+1.

#Explications précises et rigoureuses pour la fonction de l'exercice 5
#1) Créer un N tableau plein de zéros de meme taille que l'univers qu'on a ici
#2) faire deux boucles imbriqués qui parcourent le tableau A case par case
#3) Dans A chaque case a 8 voisins s'il n'est pas au bord du tableau (on additionne les valeurs que contienne ces cases pour savoir combien de voisins sont vivants
#4)ensuite faut aussi prendre en compte le cas des cases au bord du tableau mais en fait cette etape n'est pas necessaire car si on lit bien l'énoncé le problème des bords : l'espace est reférmé sur lui meme, les bords communiquent donc il suffit de faire (indice) % la_taille_du_tableau.
# En effet, on imagine que i soit notre indice, on veut aller au voisin i-1, en faisant (i-1)% n, on a :juste i-1 si i>0SI i=0, n-1et cela marchera pour i+1pas besoin de traiter les cas séparément car on a un tore
# 5) On renvoie le tableau 
    


#Q5.3
    
"""
def nb_vivants(n) : 
  U = genere_univers(n)
  for i in range(10) : 
      U = evolue(U)
  vivants = 0
  for i in range(n) : 
       for j in range(n): 
              vivants = vivants + U[i][j]
  return vivants 
"""

def nb_vivants(n) :
    """
    Entree: int,pour un certain n
    Sortie: int, nombre de cellules vivantes
    """
    U = genere_univers(n)
    for i in range (10) : 
      U = evolue(U)
    return np.sum(U)
# print(nb_vivants(20))
# print(nb_vivants(50)) 
#Pour 10 itérations, on obtient alors 
#pour k=20 :on obtient 182 dans la console en testant
#pour k=50 : on obtient 582 dans la console en testant

#Exercice 6

def generate_data() :
    global univers
    univers = evolue(univers)
    return(univers)

def update(data) :
    mat.set_data(data)
    return(mat)

def data_gen() :
    while True:
        yield generate_data()

## Test à décommenter pour comprendre
# fig, ax = plt.subplots()
# univers = genere_univers(50)
# mat = ax.matshow(generate_data()) # ici k = 50
# ani = FuncAnimation(fig, update, data_gen, interval=500)
# plt.show()
# on visualise bien l'animation dans le terminal externe
#Au bout d'un certain temps,on obtient une oscillation entre deux états


#Exercice7 
#Q1


def periode(univers) :
    """
    Entree: un tableau, un univers de départ U, par exemple genere_univers
    Sortie: un int,le temps que prend l'univers avant de tourner en boucle
    """
    Ui = univers
    Uj = evolue(univers) #car au depart Uj est Ui, mais a l'instant suivant
    i = 0
    j = 1
    while not np.array_equal(Ui,Uj) :
      if (j==2*i+1):
        i = j
        Ui = Uj #vu que l'intant i devient l'instant j
      j = j+1
      Uj = evolue(Uj)
    return j-1

#Pour le deuxieme algorithme, il y a une petite erreur de frappe
#En effet,l'erreur du sujet c'est qu'il y a pas de j dans l'histoire
#cela nous empèche d'avancer parcequ'on peut justement penser qu'on a besoin de faire le if
#du coup le j, on ne sait pas comment l'initialiser
#ni de combien on doit l'incrémenter
#En gros on ne sait pas quoi faire avec ce j
#Ainsi, grace à cette fonction, 
#On initialise Uip pour le mettre au moment ou il commence a bouclé
#Puis on initialise Ui a l'état initiale de l'univers
#on fait evoluer les deux univers a chaque fois de une unité de temps (dans la boucle)
    

def attraction(univers) :
   """
   Entree : un tableau qui représente l'univers 
   Sortie :un int, le temps qu'on doit attendre pour qu'il y ait collision entre les 2 univers
   """
   i = 0
   p = periode(univers)
   Ui = univers
   Uip = univers
   for i in range(p) :
     Uip = evolue(Uip)
   while not (np.array_equal(Ui,Uip)) :
     Ui = evolue(Ui)
     Uip = evolue(Uip)
     i = i+1
     return i

#Exercice 7  
#Q2 
     
# print(evolue((genere_univers(20))))
# print(periode(genere_univers(20)))
# print(attraction(genere_univers(20)))
     
#print(evolue((genere_univers(50))))
#print(periode(genere_univers(50)))
#print(attraction(genere_univers(50)))
#Pour k=20,en faisant le test on obtient 511 dans la console
#Pour k=50,en faisant le test on obtient 1024 dans la console et on a bien 1 minute d'attente

#Exercice 8


#Explications précises et rigoureuses de l'algorithme avant de le traduire en code Python:
#En itératif: (méthode utilisée ici)
#il faut une liste finale
#il faut une liste d'attente
#on ajoute notre case de départ à la file d'attente

#tant que la file d'attente n'est pas vite :
#  -on prend le premier élément de la file d'attente
#  -on l'ajoute à la liste finale
#  -pour tout voisin :
#    -si voisin en vie :
#      -on l'ajoute à la file d'attente


#En récursif on aurait: 
#explorer(case):
#| pour tout voisin v de case:
#|   | si v est vivant et v n'est pas dans la liste de cases explorées:
#|   |   | ajouter v à la liste des cases explorées
#|   |   | explorer(v)
    

def remplissage(u, depart):#u est l'univers
  '''
  Entrée : un tableau représentant un univers
            et les coordonnées d'une case (a,b), depart=[a,b]
  Sortie:la liste des cases appartenant au même ilot que la case (a,b)
  '''
  finale = []
  masque = np.zeros((U.shape[0],U.shape[1])) #---------------ajouté
  n=len(u)
  A=np.zeros(shape = (n,n))#tableau pour retenir les positions deja visitées
  file_attente = [depart]
  while file_attente != [] :
        elt = file_attente.pop()  #on  prend le dernier car c'est plus opti en python
        finale.append(elt)
        masque[elt[0],elt[1]]=1 #---------------ajouté
        x,y = elt
        for i in range(-1,2) :
            for j in range(-1,2):
                if (i,j)!=(0,0) :
                  v = (x+i) % n , (y+j) % n
                  if u[v[0],v[1]] == 1 :
                      if A[v[0],v[1]] == 0 :
                        file_attente.append(v)
                      A[v[0],v[1]] = 1 #on marque que que la case a été visité 
  return finale,masque==1 #---------------modifié

#print(remplissage(genere_univers(20), (1,2)))

def archipel(U):
    L_ilots = []
    M_ilots = []
    for i in range(len(U)):
        for j in range(len(U[0])):
            flag = True
            for k in range(len(M_ilots)):
                if (i,j) in L_ilots[k] :
                    flag = False
            if flag and U[i,j]==1 :
                elt = remplissage(U, (i,j))
                L_ilots.append(elt[0])
                M_ilots.append(elt[1])
    
    print(len(M_ilots))
    for i in range(len(M_ilots)):
        U[M_ilots[i]] = i+1
        for k in range(len(L_ilots[i])):
            plt.text(L_ilots[i][k][0]-0.4,L_ilots[i][k][1]+0.3, f"{i}")
    
    plt.imshow(U.transpose())
    


U = genere_univers(20)
# fig1 = plt.figure()
# plt.imshow(U.transpose())
fig2 = plt.figure()
archipel(U)




























