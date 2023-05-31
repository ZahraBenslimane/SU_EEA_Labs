#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 01:30:02 2021

@author: benaissa
"""

class Interrupteur:
    def __init__(self,courant):
        self.courant = courant
        self.etat = False  # eteint a sa creation
    
    def switch(self):
        self.etat = not (self.etat)
    


class SystemElec:
    def __init__(self,cMax,courant_interrupteurs):
        self.courantMax = cMax
        self.interrupteurs = []
        for courant_interrupt in courant_interrupteurs: # courant dans les interrupteur
            (self.interrupteurs).append(Interrupteur(courant_interrupt))
    
    def doSequence(self,sequence):
        for s in sequence:
            self.interrupteurs[s].switch()
            if self.getConso() > self.courantMax: # casse
                return False  
        return True  # fonctionnel
            
    def getConso(self):
        conso = 0
        for interrupt in self.interrupteurs:
            if interrupt.etat == True:
                conso += interrupt.courant 
        return conso
    
    
courant = [3,5,2]
courantMax = 10
sequence = [0,1,0,0,2,1]

MonSys = SystemElec(courantMax,courant)

if MonSys.doSequence(sequence) == False :
    print("le fusible est casse")
else:
    print("le fusible est fonctionnel")
    
    
courant1 = [3,5,3]
courantMax = 10
sequence = [0,1,0,0,2,1]

MonSys1 = SystemElec(courantMax,courant1)


if MonSys1.doSequence(sequence) == False :
    print("le fusible est casse")
else:
    print("le fusible est fonctionnel")
    
    
            