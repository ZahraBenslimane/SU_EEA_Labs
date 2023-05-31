# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 19:25:53 2022

@author: zahra
"""

def str2Tab(chaine):
    tab = chaine.split(',')
    res =[]
    for i,num in enumerate(tab):
        if num.isnumeric():
            res.append(int(num))
    return res


def nbInf(tabInt, n):
    nbInf = 0
    for num in tabInt:
        if num < n:
            nbInf += 1
    return nbInf

def isSup(tabInt, n):
    for i,num in enumerate(tabInt):
        if num > n :
            return i 
    if i == len(tabInt)-1:
        return -1
#declare la chaıne de caracteres ”42,142,loutre,37,13,857”
chaine ="42,142,loutre,37,13,857"; 
#la convertit en un tableau d’entiers tabInt et affiche le resultat
tab = str2Tab(chaine);print(tab)    

n1 = int(input("Veuillez saisir un entier n1: "))
print("Le nombre d'entiers inférieurs à {} est : {}\n".format(n1,nbInf(tab,n1)))

n2 = int(input("Veuillez saisir un entier n2: "))
print("la position du premier entier superieur à {} est : {}\n".format(n2,isSup(tab,n2)))        
      


#%%   Exo 2

from abc import ABC, abstractmethod

class Personne(ABC):
      (import, attributs, methodes)



