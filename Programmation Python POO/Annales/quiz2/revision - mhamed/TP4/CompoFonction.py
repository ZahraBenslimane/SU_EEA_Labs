#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 00:14:26 2021

@author: benaissa
"""
from Fonction import Fonction

class CompoFonction(Fonction):
    def __init__(self,f,g):
        
            self.f = f
            self.g = g
        
    def __str__(self):
        #aff =  self.f.__str__()
        #aff += self.g.__str__()
        
        return "fog"
         
    def getValeur(self,x):
        gx =  self.g.getValeur(x)
        val = self.f.getValeur(gx)
        return val
    
    def getDerivee(self, x):
        dgx = self.g.getDerivee(x)
        dfgx = self.f.getDerivee(self.g.getValeur(x))
        der = dgx*dfgx
        return der
    