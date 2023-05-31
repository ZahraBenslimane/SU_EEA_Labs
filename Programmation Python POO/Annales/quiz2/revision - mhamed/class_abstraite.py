#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:33:17 2021

@author: benaissa
"""

# class abstraite
from abc import ABC,abstractmethod
import datetime
class Vehicule(ABC): # classe abstraite   # il faut pas l'intancier elle même, si y'aura une methode qu'on ne connais pas, ou bien il faut mettre taxe = 0 par defaut
    
     def __init__(self,marque,annee):
         self.__marque = marque    # privé : appel avec un setter
         self.__annee = annee   # privé : appel avec un setter
     
     def Age (self): 
         now = datetime.datetime.now()
         return now.year - self.annee
     def who(self):
         return "Vehicule"
         
         
     @property
     def annee(self):
         return self.__annee 
     @annee.setter
     def annee(self,annee):
         #now = datetime.datetime.now()
         #if (annee>1900) and (annee <= now.year): 
         self.__annee = annee # on la stocke directement comme elle est
     @property 
     def marque(self):
         return self.__marque
     @marque.setter        
     def marque(self,marque):
         self.__marque = marque
     
     def __str__(self):
         res = self.who( ) + " - marque " + self.marque
         res += " construit en " + str( self.annee )
         return res
     @abstractmethod
     def taxe(self):
         pass
     
class Voiture(Vehicule):
    def __init__(self,marque,annee,puissance):
        super().__init__(marque,annee) 
        self.__puissance = puissance
    def who(self):
    
        return "Voiture"
    def __str__(self):
        res = super().__str__()
        res += " de puissance " + str( self.puissance ) + " CV" 
        return res
    def taxe(self):
        #return self.puissance *10 +50
        return self.puissance * 10. + (self.annee - 1900) 
    
    @property
    def puissance(self):
        return self.__puissance
    @puissance.setter
    def puissance(self,puissance):
        self.__puissance = puissance
        
        
Voit1 = Voiture("Ferrari",2015, 450)
print("type :", Voit1.who())
print(Voit1)
print("taxe = ",Voit1.taxe())
print("age = ",Voit1.Age())  # la fonctioon age s'est adaapté en finction du type