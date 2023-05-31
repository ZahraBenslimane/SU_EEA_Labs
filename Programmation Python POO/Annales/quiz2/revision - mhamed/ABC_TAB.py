# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 14:19:26 2021

@author: zahra
"""

class A :
    def __init__(self,a):
        self.__a = a
        
    @property    
    def m1(self):
        return self.__a
    
    
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        self.__b = b
      
    @property    
    def m1(self):
        return super().m1 + self.__b
    
    
class C(A):
    def __init__(self,a,c):
        super().__init__(a)
        self.__c = c
      
    @property    
    def m1(self):
        return super().m1 + self.__c
    
class Tab:
    def __init__(self,t):
        self.t = t
        
    def __str__(self):
        nbA = 0 ; nbB = 0; nbC = 0
        sA = 0; sB = 0 ; sC = 0
        for obj in self.t : 
            if  isinstance(obj, B):
                nbB += 1 
                sB += obj.m1
            elif isinstance(obj, C):
                nbC += 1
                sC += obj.m1
            elif isinstance(obj,A):
                nbA += 1
                sA += obj.m1
        res = "A: ({}, {})\n".format(nbA,sA)
        res += "B: ({}, {})\n".format(nbB,sB)
        res += "C: ({}, {})\n".format(nbC,sC)         
        return res
                
    
choix = [2,1,1,0,1,1,0,2,0,2,2,1,0,0,2,2,2,2,2,0]
vA = [-3,-5,0,4,0,2,1,-1,-4,2,-5,1,-3,2,-4,-4,2,-3,-3,1]
vB = [-1,3,2,0,4,2,2,5,4,-1,-5,1,-3,1,-3,0,-4,-4,0,-3]
vC = [-5,4,-4,2,-2,3,1,4,4,-5,-1,4,1,5,5,-3,-2,-2,-3,-5]

        
t = []

for i,monChoix in enumerate(choix) : 
    if monChoix == 0:
        t.append( A(vA[i]) )
    elif monChoix == 1:
        t.append( B(vA[i], vB[i]) )
    elif monChoix == 2:
        t.append( C(vA[i], vC[i]) )
        
myTab = Tab(t)        

print(myTab)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         