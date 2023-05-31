# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:42:01 2021

@author: zahra
"""

from abc import ABC, abstractmethod

class A(ABC):
    def __init__(self,a):
        self.a = a
    @abstractmethod
    def m1(self,x): pass


class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.b = b
        
    def m1(self,x):
        return self.a * x + self.b
        
monB = B(3,4)

print(monB.m1(5))