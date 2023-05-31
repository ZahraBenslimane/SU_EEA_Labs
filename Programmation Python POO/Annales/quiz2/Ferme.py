# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 09:05:15 2021

@author: zahra
"""


class Cage:
    
    def __init__(self, nSains, nMalades):
        self.nSains = nSains
        self.nMalades = nMalades
        
        
    def nextYear(self):
        if self.nSains > 2 * self.nMalades:
            self.nSains -= 2* self.nMalades
            self.nMalades = 2 * self.nMalades
            
        elif 0 < self.nSains <= 2 * self.nMalades:
            self.nMalades += self.nSains
            self.nSains = 0
            
        elif self.nSains == 0:
            self.nMalades = 0 

    def nAlive(self):
        return self.nSains + self.nMalades
  
        
class Ferme : 
    def __init__(self,cages):
        self.cages = []
        for c in cages :
            self.cages.append(Cage(c[0],c[1]))
            
    def nextYear(self):
        for c in self.cages:
            c.nextYear()
        
    def isAlive(self):  
            if all( c.nAlive() == 0 for c in self.cages):
                return False
            else:
                return True
           
y = 10

#cages = [ [5,2], [20,1],[37,13],[1428,57]]

cages = [[16,2],[8,6],[50,0]] 

maFerme = Ferme(cages)     

for i in range(y):
    maFerme.nextYear()

if maFerme.isAlive() == False:
    print("Apres {} annee(s), la ferme est morte".format(y))
else:
    print("Apres {} annee(s), la ferme est vivante".format(y))
    
