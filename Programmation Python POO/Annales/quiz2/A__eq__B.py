# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:46:54 2021

@author: zahra
"""


class B:
    def __init__(self, b):
        self.b = b
        
    def __eq__(self,other):
        
        if not isinstance(other,B):
            return False
        elif self is other:
            return True
        else :
            return self.b == other.b
        
        
    def __str__(self):
        return "{}".format(self.b)
            
class A :
    def __init__(self,a,vB):
        self.a = a
        self.vB = vB
    
    def __eq__(self,other):
        if not isinstance(other,A):
            return False
        if (self is other ):
            return True
        else:
            return self.vB == other.vB and self.a == other.a
            
        
a1, b1 = 0, 9
a2, b2 = 0, 9

aTest1 = A(a1,B(b1))
aTest2 = A(a2,B(b2))

print(aTest1 == aTest2)

