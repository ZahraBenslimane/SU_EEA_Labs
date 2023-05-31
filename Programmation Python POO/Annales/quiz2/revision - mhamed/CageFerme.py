#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:32:15 2021

@author: benaissa
"""

class Cage:
    def __init__(self,nSains,nMalades):
        self.nSains = nSains
        print("nSain = ",self.nSains)
        self.nMalades = nMalades
        print("nMalades = ", self.nMalades)
    
    def nextyear(self):
        if self.nSains > 2*self.nMalades:           
            self.nSains = self.nSains - 2* self.nMalades
            self.nMalades += self.nMalades
        elif 0 < self.nSains < 2*self.nMalades:
            self.nSains = 0
            self.nMalades = self.nSains
        elif self.nSains == 0:
            self.nMalades = 0
        
        
    def nAlive(self):
        return self.nSains + self.nMalades


class Ferme:
    def __init__(self,cages):
        self.cages = []
        
        if type(cages[0]) == str : 
            for couple in cages :
                nS = int((couple.split())[0])
                nM = int((couple.split())[1])
                self.cages.append(Cage(nS,nM))
            
        if type(cages[0][0] ) == int: 
            for couple in cages :              
                self.cages.append(Cage(couple[0],couple[1]))
    def nextYear(self):
        for cage in self.cages:
            cage.nextyear()
            
    def isAlive(self):
        for cage in self.cages:
            if cage.nAlive() > 0 :
                return True
        return False
            
y = 10

cages1 = ["5 2", "20 1", "37 13", "1428 57"]
cages2 = [[16,2],[8,6],[50,0]]

Ferme1 = Ferme(cages1)
Ferme2 = Ferme(cages2)


for i in range(1,y):
    if Ferme1.isAlive() == False:
        print("Apres {} annee(s), la ferme est morte".format(i))
        break
    else :
        Ferme1.nextYear()
    
if Ferme1.isAlive() == True:
    print("Apres {} annee(s), la ferme est vivante".format(y))
    
    
for i in range(1,y):
    if Ferme2.isAlive() == False:
        print("Apres {} annee(s), la ferme est morte".format(i))
        break
    else :
        Ferme2.nextYear()
    
if Ferme2.isAlive() == True:
    print("Apres {} annee(s), la ferme est vivante".format(y))
    
    


