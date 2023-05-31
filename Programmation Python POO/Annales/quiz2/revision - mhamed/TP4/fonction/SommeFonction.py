#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 20:33:24 2021

@author: benaissa
"""

from Fonction import Fonction


class SommeFonction(Fonction):
    def __init__(self,fonction):
        if len(fonction) >10 :
            print("c'est limité à 10 fonctions")
        else:
            self.fonction = fonction
            
    def __str__(self):
        aff = ""
        for i in range (len(self.fonction)):
            if i != 0 and i != len(self.fonction)-1:
                aff += " + "
            aff += self.fonction[i].__str__()  
        return aff
            
    def getValeur(self,x):
        val = 0
        for i in range (len(self.fonction)):
            val += self.fonction[i].getValeur(x)
        return val
    def getDerivee(self, x):
        der = 0
        for i in range (len(self.fonction)):
            der += self.fonction[i].getDerivee(x)
        return der
    
            
