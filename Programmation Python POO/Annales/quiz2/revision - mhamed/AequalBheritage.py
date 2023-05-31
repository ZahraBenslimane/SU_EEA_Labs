#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:52:52 2021

@author: benaissa
"""

class A:
    def __init__(self,a):
        self.__a = a
    def __eq__(self, other):
        if not isinstance(other,A):
            return False
        if self is other:
            return True
        return self.__a == other.__a
    
    
class B(A):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def __eq__(self,other):
        if not isinstance(other,B):
            return False
        if self is other:
            return True
        return (self.__a == other.__a and self.__b == other.__b)

a1 = A(2)
a2 = A(3)
a3 = A(3)
a4 = a3

b1 = B(1,1)
b2 = B(2,2)
b3 = B(1,1)
b4 = b2

print(a1 == a2)
print(a3 == a2)
print(a3 == a4)

print("--------")

print(b1 == b2)
print(b1 == b3)
print(b4 == b2)




