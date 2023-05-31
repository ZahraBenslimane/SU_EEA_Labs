#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 02:24:50 2021

@author: benaissa
"""

class A:
    def __init__(self,a):
        self.a = a
    def __str__(self):
        res = "A: a = "+ str(self.a)
        return res
    def who(self):
        if isinstance(self,B):
            return "B"
        elif isinstance(self,A):
            return "A"
    
class B(A):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self):
        res = "B: a = {}, b = {}".format(self.a,self.b)
        return res
        
    def who(self):
        if isinstance(self,B):
            return "B"
        elif isinstance(self.A):
             return "A"
        
choix = [1,0,1,1,0,1,1,0]
a = [2,-4,-3,5,-2,4,-4,-1]
b = [5,-2,2,-1,4,-2,4,-5]

AA = []
for v in a:
    AA.append(A(v)) 

BB = []
for i,v in enumerate (a):
    BB.append(B(v,v)) 

for i,n in enumerate(choix):
    if n == 0:
        print(AA[i])
 
for i,n in enumerate(choix):
    if n == 1:   
        print(BB[i])
        

print("--------------")
choix1 = [0,1,0]
a1 = [-2,-3,4]
b1 = [-2,5,1]


AA1 = []
for v in a1:
    AA1.append(A(v)) 

BB1 = []
for i,v in enumerate (a1):
    BB1.append(B(v,v)) 

for i,n in enumerate(choix1):
    if n == 0:
        print(AA1[i])
 
for i,n in enumerate(choix1):
    if n == 1:   
        print(BB1[i])

        
        