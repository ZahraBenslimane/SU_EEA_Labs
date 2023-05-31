#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 11:38:12 2021

@author: benaissa
"""

#  revision héritage Cours 3
import datetime

class Vehicule : 
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
        
class Voiture(Vehicule):  # héritage de Vehicule de tout mais a accèss à ce qui est public, Voiture n'a pas accès au attributs privé de Vehicule 
    def __init__(self,marque,annee,puissance):
        super().__init__(marque,annee)  # il est deja défini donc il va initialisé annee et marque
        self.__puissance = puissance
    def who(self):
        #super.who(self)  # je veux pas afficher l'ancienne mais juste la rédifinir donc pas la peine cette ligne 
        return "Voiture"
    def __str__(self):
        res = super().__str__()
        res += " de puissance " + str( self.puissance ) + " CV" 
        return res
    def taxe(self):
        #return self.puissance *10 +50
        return self.puissance * 10. + (self.annee - 1900)  # ça marche puisque j'ai un getter
    @property
    def puissance(self):
        return self.__puissance
    @puissance.setter
    def puissance(self,puissance):
        self.__puissance = puissance
        
        
# main pour le test :

Voit1 = Voiture("Ferrari",2015, 450)
print("type :", Voit1.who())
print(Voit1)
print("taxe = ",Voit1.taxe())
print("age = ",Voit1.Age())  # la fonctioon age s'est adaapté en finction du type

print("interet Polymorphisme, on peut ajouter des voiture dans un tableau de vehicule psq voiture est un vehicule, le coontraire est faut")

tab = [ ] # Tableau vide
tab.append( Voiture( "Renault",2014, 5 ) ) 
tab.append( Vehicule( "Rockrider" , 2005,) )
tab.append( Voiture(  "Peugeot",2012, 3 ) ) 
tab.append( Vehicule(  "Airbus",2015 ) ) 
tab.append( Vehicule( "MAN", 2010 ) )
for v in tab :
    print( v )



