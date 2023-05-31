#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:17:13 2021

@author: benaissa
"""
# Partie Exo 1
from Fonction import Fonction

class Polynome(Fonction) :
    def __init__(self, coefficients):
        self.__coefficients = coefficients
    def __str__(self):
        n = len(self.coefficients)
        res = ""
        for i in range(n-1,0,-1):
            if self.coefficients[i] >= 0  and i != n-1:     
                res += " + "   
            res += " "+ str(self.coefficients[i])+" x^"+str(i)
        if self.coefficients[0] >= 0:
            res += " + "   
        res += str(self.coefficients[0])
        
        res+= " "
        return res
    
    def getDegree(self):
        n = len(self.coefficients)
        if self.coefficients[n-1] != 0: #   aa confirmer
            return n-1
        
        else : 
            n = n-1
            while( self.coefficients[n] == 0):
                n = n-1
            return n
    def getValeur(self,x):
        val = 0
        for i in range(len(self.coefficients)):
            val+= self.coefficients[i]* x**i
        return val
        
    def getDerivee(self,x):
        der = 0
        for i in range(1,len(self.coefficients)):
            der+= i* self.coefficients[i]* x**(i-1)
        return der
    
    def __eq__(self,other):
        if not isinstance(other,Polynome):
            return False
        if self is other:
            return True
        
        n1 = len(self.coefficients)
        n2 = len(other.coefficients)
        if (n1 == n2):   
            for i in range(n1): 
                if self.coefficients[i] != other.coefficients[i]:
                    return False
            return True
        else: 
             nmin = min (n1,n2)
             nmax = max(n1,n2)
             for i in range(nmin):  
                 if self.coefficients[i] != other.coefficients[i]:
                     return False
                 
             p = self.coefficients
             
             if n2 > n1 :
                 p = other.coefficients
             for i in range(nmin+1,nmax):
                 if p[i] != 0:
                     return False
             return True
    
    
    
    @property   # getter
    def coefficients(self):
        return self.__coefficients 
    @coefficients.setter
    def coefficients(self,coefficients):
        self.__coefficients = coefficients
    
