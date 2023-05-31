# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 13:57:30 2021

@author: zahra
"""

class SystemeElec :
    def __init__(self,courantMax,courantsInterrupteurs):
        self.courantMax = courantMax
        self.interrupteurs = []
        for courant in courantsInterrupteurs:
            (self.interrupteurs).append( Interrupteur(courant) )
        
    def doSequence(self,sequence):            
        for s in sequence:           
            self.interrupteurs[s].switch()
            if self.getConso() > self.courantMax:
                return False
        return True
            
    def getConso(self):
       sommeConso = 0
       for interrupt in self.interrupteurs :
            if interrupt.etat == True :
                #print(interrupt.courant)
                sommeConso += interrupt.courant
       #print("s = ",sommeConso)
       return sommeConso
             
    
class Interrupteur :
    def __init__(self,courant):
        self.etat = False
        self.courant = courant
        
    def switch(self):
        self.etat = not(self.etat)       
        

#courant = [3,5,2]
#courantMax =10
#sequence = [0,1,0,0,2,1]

courant = [3,5,3]
courantMax =10
sequence = [0,1,0,0,2,1]

"""
interrupteurs = []
for c in courant:
    interrupteurs.append(Interrupteur(c))
"""
   
mySys =  SystemeElec(courantMax,courant)  

#print(mySys.doSequence(sequence) )
    
if mySys.doSequence(sequence):
    print("Le fusible est fontionnel\n")
else:
    print("Le fusible est casse\n")
    