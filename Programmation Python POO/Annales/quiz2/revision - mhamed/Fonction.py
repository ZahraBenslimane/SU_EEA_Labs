#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:08:20 2021

@author: mhamed
"""

class Fonction : 
    def __init__( self , a , b , x) : 
        self.__a = a
        self.__b = b
        self.__x = x
    
    @property
    def x (self ) : 
        return self.__x
    @x.setter
    def x(self , new_x) : 
        if  self.__a <= new_x <=self.__b : 
            self.__x = new_x
        else : 
            print ("Erreur x doit etre compris entre {} et {}".format(self.__a , self.__b))
    
    def __str__(self) : 
        return ("Fonction({}, {}, {})".format(self.__a , self.__b , self.__x))

    
a , b = -7, 6
x = 2
newX= [-3 , -2 , 6 , -10 , -6 , 6 ]

t=Fonction(a , b , x)   
#print (t)
for i in newX : 
    t.x=i
    print (t)

#%%