# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:00:20 2020

@author: User
"""

import numpy as np# Préfixe np à utiliser pour importer toutes les fonctions 
"""partie a"""
chaine1="test"
print(id(chaine1))
chaine2=chaine1.replace("t","r")
print(chaine2)
print(id(chaine2))
T1=np.array([0,1,2,3])
print(T1.dtype)
L1=[0,1,2,3]
T2=np.array([[0,1,2,3],
             [4,5,6,7]])
print(T2)
L2=[(0,1,2,3),(4,5,6,7)]
L3=2*L1
T3=2*T1
T4=np.array(T1,dtype ="uint8")
print(T4)

"""partie b"""
T5=np.linspace(0,4,5)#(départ,fin,nbre de points)

T6=np.arange(0,5,1)#(départ,fin,incrément)

T7=np.zeros((2,3))#((nbre de lignes, nbre de colonnes))
s=np.sum(T1)

lignes,colonnes=np.shape((T7)) #renvoie un tuple(nbre lignes, nbre colonnes)
lignes= np.shape((T7))[0]
""
T8=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(T8[1])#renvoie la ligne d'index 1
print(T8[-1])#renvoie la dernière ligne
print(T8[1,2])#renvoie le motif en 2e ligne et 3e colonne 
print(T8[1,:])#renvoie la ligne d'index 1
print(T8[1,:-1])#renvoie la ligne d'index 1 sans le dernier élément
print(T8[:,1])#renvoi tout le colonne d'index 1
print(T8[1:3,1:3])#[index 1e ligne:index de la dernière ligne exclue,index 1e colonne:index de la dernière colonne exclue]
print(T8[-1:-5:-1,-1:-5:-1])#début,fin pas =-1 pour donner le sens
print(T8[[True,False,False],:])#permet de ne conserver que la 1e ligne
"""partie c"""
import time
import matplotlib.pyplot as plt
import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[9,8,7],[6,5,4],[3,2,1]])
C=np.zeros((3,3))
for i in range (3):
    for j in range (3):
        C[i,j]=A[i,j]+B[i,j]
print(C)
C[:,:]=A[:,:]+B[:,:]
print(C)

temps1=[]
liste_N=[2000,3000,4000]
for N in liste_N:
    A=np.random.randint(10,size=(N,N))
    B=np.random.randint(10,size=(N,N))
    t_debut1=time.time()
    C=np.zeros((N,N))
    for i in range (N):
        for j in range (N):
            C[i,j]=A[i,j]+B[i,j]
    temps1.append(time.time()-t_debut1)

temps2=[]
for N in liste_N:
    A=np.random.randint(10,size=(N,N))
    B=np.random.randint(10,size=(N,N))
    t_debut2=time.time()
    C=np.zeros((N,N))
    C[:]=A[:]+B[:]
    temps2.append(time.time()-t_debut2)


plt.plot(liste_N,temps1)
plt.axis([900,5000,0,10])
plt.ylabel("temps d'exécution (s)")
plt.xlabel("Valeurs de N")
plt.title("somme de deux tableaux avec boucles for")
plt.grid()
plt.show()
plt.plot(liste_N,temps2)
plt.axis([900,5000,0,0.1])
plt.ylabel("temps d'exécution (s)")
plt.xlabel("Valeurs de N")
plt.title("somme de deux tableaux avec la vectorisation")
plt.grid()
plt.show()