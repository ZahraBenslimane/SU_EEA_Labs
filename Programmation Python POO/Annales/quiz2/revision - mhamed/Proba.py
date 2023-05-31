#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 12:16:09 2021

@author: benaissa
"""
from math import exp
from abc import ABC, abstractmethod

class Distribution(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def getProba(self,x):
        pass
    @abstractmethod
    def getRepartition(self,x):
        pass
    
class Uniforme(Distribution):
    def __init__(self,a,b):
        if a > b :
            print("Erreur: a > b")
            c = a
            a = b
            b = c
        self.a = a
        self.b = b
    def getProba(self,x):
        if x > self.b :
            return 0.0000
        elif x < self.a:
            return 0.0000
        return 1/(self.b-self.a)
    def getRepartition(self,x):
        if x > self.b :
            return 1.0000
        elif x < self.a:
            return 0.0000
        return (x - self.a)/ (self.b - self.a)
    
    
class Exponentielle(Distribution):
    def __init__(self,l):
        if l <=  0 :
            print("Erreur: lamda <= 0")
            l = abs(l)
        self.l = l
    def getProba(self, x):
        if x < 0 :
            return 0
        return self.l*exp(-self.l*x)
    def getRepartition(self, x):
        if x < 0 :
            return 0
        return (1-exp(-self.l*x))
    
choix = [1,1,0]
a = [3.9143,-4.7348,-2.7584]
b = [-4.9007,-3.1052,0.0490]
l = [0.5648,3.9402,0.9801]
x = 0.2395

tE = []
tU = []
for i,c in enumerate(choix):    
    if c == 1 :
        E = Exponentielle(l[i])
        tE.append(E)
        tU.append(0)
    elif c == 0:
        U = Uniforme(a[i],b[i])
        tU.append(U)
        tE.append(0)
        
for i,c in enumerate(choix):
    if c == 1 :        
        print("(%.4f " % tE[i].getProba(x) ,", %.4f)"   % tE[i].getRepartition(x)) 
    elif c == 0:
        print("(%.4f " % tU[i].getProba(x) ,", %.4f)"   % tU[i].getRepartition(x)) 
        
        
choix1 = [0,0,0,1,1,1,1,0,1,0]
a1 = [-3.5699, -4.5395,0.7218,2.8704,3.1865,-0.0843, -1.1969,-1.0690,-3.7374,2.8157]
b1 = [-0.6369,0.5637,4.9995,0.1526,-4.3240,-1.1375,2.2094,-2.9230,-4.9922,-2.0239]
l1 = [-1.0594,-4.8751,-2.8339,2.0033,-1.8983,-4.2137,-3.5531,-4.4080,-1.3887,-1.1563]
x1 = 4.8787      
    

tE1 = []
tU1 = []
for i,c in enumerate(choix1):    
    if c == 1 :
        E = Exponentielle(l1[i])
        tE1.append(E)
        tU1.append(0)        
    elif c == 0:
        U = Uniforme(a1[i],b1[i])
        tU1.append(U)
        tE1.append(0)

for i,c in enumerate(choix1):
    if c == 1 :
        
        print("(%.4f " % tE1[i].getProba(x1) ,", %.4f)"   % tE1[i].getRepartition(x1)) 
    elif c == 0:
        print("(%.4f " % tU1[i].getProba(x1) ,", %.4f)"   % tU1[i].getRepartition(x1)) 
        
    
    
    
    