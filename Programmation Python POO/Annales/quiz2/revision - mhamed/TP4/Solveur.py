#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:08:31 2021

@author: benaissa
"""

# Parttie Exo 2 : 
    
class Solveur:
    def __init__(self,f,precision):
        self.__f = f
        self.__precision = precision
     
    @property
    def f(self):
        return self.__f
    @f.setter
    def f(self,f):
        self.__f= f
    @property 
    def precision(self):
        return self.__precision 
    @precision.setter
    def precision(self,precision):
        self.__precision = precision
    
    
    def newton(self, x0):
        uN = self.precision +1
        n = 0
        while (self.f.getValeur(x0) != 0) and (abs(uN) > self.precision) and n < 1000 :
            uN = self.f.getValeur(x0)/self.f.getDerivee(x0)
            x0 = x0 - uN 
            
            n += 1
            if n == 1000 :   # pour régler le probleme de non existante de solution sur IR on limite le nombre d'itération
                print("il ne y'a pas de zero")
                break    
        return x0
    
    def dichotomie(self,a,b):
        fA = self.f.getValeur(a)
        fB = self.f.getValeur(b)
        c = (a+b)/2
        fC = self.f.getValeur(c)
        if fA == 0:
            return a
        elif fB == 0:
            return b
        else : 
            n = 0
            while (abs(b-a) > self.precision and fC != 0 and n < 1000):
                c = (a+b)/2
                fC = self.f.getValeur(c)
                if fA*fC <0 :
                    b = c
                    fB = fC
                else :
                    a = c
                    fA = fC  
                n += 1
                if n== 1000 :
                    print("il ne y'a pas de zero")
                    break
            return c
 