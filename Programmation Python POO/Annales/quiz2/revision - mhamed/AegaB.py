#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:53:47 2021

@author: benaissa
"""
class B : 
    def __init__(self,b):
        self.b = b
    def __eq__(self,other):
        if not isinstance(other,B):
            return False
        if self is other:
            return True
        return self.b == other.b

class A :
    def __init__(self,a,vB = B(0)): # j'ai ajouté une valeur par defaut
        self.a = a
        self.vB = vB
        
    def __eq__(self,other):
        if not isinstance (other,A):
            return False
        if self is other:
                return True
        if self.a != other.a:
            return False
        return self.vB == other.vB
               

    
    
    
a1,b1 = 0,9
print(A(a1) == A(b1))

