# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:01:16 2020

@author: User
"""

import numpy as np
from PIL import Image

"""création d'un tableau numpy associée à une image PNG"""
photo=Image.open("pomme.jpg")
tab=np.array(photo)#tableau tridimensionnel
H,l,p=np.shape((tab))#H = nombre de lignes, l = nombre de colonnes, p = nombre de couleurs
print(H,l,p)
print(tab)

"""question 1"""
def image_rouge(tab):
    for i in range(H):
        for j in range (l):
            for k in (1,2) :
                tab[i,j,k]=0
    return tab
def image_rouge2(tab):
    tab[:,:,1:3]=0
    return tab
"""création d'une image PNG à partir d'un tableau numpy"""
"""question2"""
photo2=Image.fromarray(image_rouge2(tab))
photo2.save("photo_nouvelle.jpg") # pour l'enregistrer au format voulu
photo2.show()



