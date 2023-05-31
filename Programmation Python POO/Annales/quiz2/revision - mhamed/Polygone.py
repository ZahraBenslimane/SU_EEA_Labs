#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 20:09:12 2021

@author: benaissa
"""

class Point :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        res = "({}, {})".format(self.x,self.y)
        return res
    
class Polygone :
    def __init__(self,x,y):
        
        if (len(x) != len(y)):
            print("Erreur: x et y de tailles differentes")
            self.n = min(len(x),len(y))
            # self.x = x
            # self.y = y
            
        else :
            self.n = len(x)
            # self.x = x
            # self.y = y
        self.sommets = []
        for i in range(self.n): 
            self.sommets.append( Point(x[i],y[i]) )
    
        
    def __str__(self):
        res = "Polygone a {} sommets: ".format(self.n)
        for point in self.sommets:
            if point != self.sommets[-1]:
                res +=  point.__str__() + ", " #" ({}, {}),".format(self.x[i],self.y[i]) 
            else :
                res +=    point.__str__()  #" ({}, {})".format(self.x[i],self.y[i])
        return res
        
x = [1,4,2]
y = [8,5,7]     

P = Polygone(x,y)
print(P)

x1 = [-2,10,-10,-8,10,-9,-3,-8,-2,8,-8,-9]
y1 = [-10,5,4,1,-1,-10,-9,-10,-5,10,-6,-6]

P1 = Polygone(x1,y1)
print(P1)

x2 = [-5,6,-8,7,9,3,-1,-8,10,-10,1,-5,0]
y2 = [10,-4,10,-3,4,6,-8,2]


P2 = Polygone(x2,y2)
print(P2)
  
        
        