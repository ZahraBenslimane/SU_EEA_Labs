#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 01:16:15 2021

@author: benaissa
"""
from abc import ABC,abstractmethod

class A(ABC):
    def __init__(self,a):
        self.a = a
        
    @abstractmethod
    def m1(self,x):
        pass
    
class B(A):
    def __init__(self,a,b):
        self.b = b
        self.a = a # elle herite l'attribut
    def m1(self,x):
        return self.a * x + self.b
    
choix = 1
a,b =  3,4
x = 5
B1 = B(a,b)

if choix == 1:
    print(B1.m1(x))
elif choix == 0:
    A1 = A(a)  #il faut pas que ça marche