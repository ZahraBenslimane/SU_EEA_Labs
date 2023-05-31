# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:02:18 2021

@author: zahra
"""

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        res = "({},{})".format(self.x,self.y)
        return res
    
class Polygone:
    def __init__(self,x,y):
        if len(x) != len(y):
            print("Erreur: x et y de tailles differentes")
        self.n =  min(len(x),len(y))
        self.sommets = []
        for i in range(self.n):
            self.sommets.append(Point(x[i],y[i]))

    def __str__(self):
        res = "Polygone a {} sommets: ".format(self.n)
        for s in self.sommets:
            if s == self.sommets[-1]:
                res+= "{}".format(s.__str__())
            else:     
                res+= "{}, ".format(s.__str__())
        return res
        
    
x = [1,4,2]
y = [8,5,7]    

x1 = [-2,10,-10,-8,10,-9,-3,-8,-2,8,-8,-9]
y1 = [-10,5,4,1,-1,-10,-9,-10,-5,10,-6,-6]
    
x3 = [-5,6,-8,7,9,3,-1,-8,10,-10,1,-5,0]
y3 = [10,-4,10,-3,4,6,-8,2]
    
myPoly = Polygone(x3,y3)

print(myPoly)
print("\n")  