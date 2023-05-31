#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:14:56 2021

@author: benaissa
"""
#ax+b
#ax

class A:
    def __init__(self,a):
        self.__a = a
    def __str__(self):
        return ("A: a = {}".format(self.__a))
    def who(self):
        return "A"
    def m1(self,x):
        return self.__a*x
    
    
class B(A):
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
        
    def __str__(self):
        return ("B: a = {}, b = {}".format(self.__a,self.__b))
    def who(self):
        return "B"
    def m1(self,x):
        return self.__a*x + self.__b
    
    
choix = [1,0,1]
a,b = [-4,-1,0], [0,1,-4]
x = -2

tab = []
for i,c in enumerate(choix):
    if c == 0:
        tab.append(A(a[i]))
    elif c==1 : 
        tab.append(B(a[i],b[i]))
        
res = ""        
for i,v in enumerate (tab):
    if v.who() == "A":
        if i == 0:
            res += v.__str__() +  ","
        elif  0<i< len(tab)-1:
            res += " "
            res += v.__str__() + ","
        else : 
            res += " "
            res += v.__str__() 
        
    elif v.who() == "B":
        #res += v.__str__()
        if i == 0:
            res += v.__str__() +  ","
        elif  0<i< len(tab)-1:
            res += " "
            res += v.__str__() + ","
        else : 
            res += " "
            res += v.__str__() 
   
  
print("["+res+"]")
for i,v  in enumerate(tab):
    print("m1[{}] = {}".format(i,v.m1(x)))
    
    
    
    
    
    

    

        