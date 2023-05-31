#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:35:05 2021

@author: benaissa
"""

# programme principale 

from Polynome import Polynome
from Sinus import Sinus
from Exponentielle import Exponentielle
from SommeFonction import SommeFonction
from Solveur import Solveur

from CompoFonction import CompoFonction


coeff = [1.2,-0.1,-1.3,0.1,0.1]
    
p = Polynome(coeff)

e = Exponentielle(-1,0.2)

s = Sinus(1,1/5,0)


print(p)
print(e)
print(s)

# calcul des fonction en différent point
print("degree",p.getDegree())
print("----------------------")
print("calcul des valeur pour x=1")
print(p.getValeur(1))
print(e.getValeur(1))
print(s.getValeur(1))
print("----------------------")
print("calcul des valeur pour x=0")
print(p.getValeur(0))
print(e.getValeur(0))
print(s.getValeur(0))
print("----------------------")
print("calcul des derivees pour x=1")
print(p.getDerivee(1))
print(e.getDerivee(1))
print(s.getDerivee(1))
print("----------------------")
print("calcul des derivees pour x=0")
print(p.getDerivee(0))
print(e.getDerivee(0))
print(s.getDerivee(0))

print("------------------------")
print("test SommeFonction")
som = SommeFonction([p,s,e])
print("(p+s+e)(x) = ",som)
print("calcul pour différentes valeurs de x :")
print("(p+s+e)(1) = ",som.getValeur(1))
print("(p+s+e)(-2) = ",som.getValeur(-2))
print("(p+s+e)(0) = ",som.getValeur(0))

print("------------------------")
print("calcul de la dérivé pour différentes valeurs de x :")
print("(p+s+e)'(1) = ",som.getDerivee(1))
print("(p+s+e)'(-2) = ",som.getDerivee(-2))
print("(p+s+e)'(0) = ",som.getDerivee(0))



# EXO 2 

Solver1 = Solveur (som,1e-5)

print("solution avec la methode de newton :")
print(Solver1.newton(2))

print("solution avec la methode de dichottomie :")
print("dans l'interval [0,2]")
print(Solver1.dichotomie(0,2)) 
print("dans l'interval [2,4]")
print(Solver1.dichotomie(2,4)) 


# EXO 3
# j'ai crée une class >COmpoFoncttion qui herite de fonction

print("------------------------")
print("Composition de fonction ")
fog = CompoFonction(p,s)


print(fog)
Solver2 = Solveur (fog,1e-5)
print("solution avec la methode de newton :")
print(Solver2.newton(2))










