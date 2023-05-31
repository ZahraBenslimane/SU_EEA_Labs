#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 19:20:56 2021

@author: benaissa
"""


# classe abstraite psq les methode change avec le type de fonction
# on peut pas definir __str__ comme une fonction abstraite --> on l'a declare pas
# pour le constructeur --> il fais rie, même si on l'heris-te on va pas l'utiliser  normalement !!!

from abc import ABC, abstractmethod

class Fonction(ABC):
    
    #@abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def getValeur(self,x):
        pass
    @abstractmethod
    def getDerivee(self,x):
        pass
    
        