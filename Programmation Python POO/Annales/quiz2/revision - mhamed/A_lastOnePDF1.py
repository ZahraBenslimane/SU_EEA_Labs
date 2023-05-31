# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 15:16:23 2021

@author: zahra
"""


class A:
    
    def __init__(self,val,code):
        #self.__val = val
        self.__val = val
        self.__code = code
        self.__nTentatives = 0
        
    @property
    def val(self):
        return self.__val
    
               
    @val.setter 
    def val(self,valCode):
        val = valCode[0]
        code = valCode[1]
        
        self.__nTentatives += 1
        
        if 3 >= self.__nTentatives > 0 and code == self.__code:
            self.__val = val
            self.__nTentatives = 0
            print("Code vrai: val a été modifié ")
        elif 3 >= self.__nTentatives > 0 and code != self.__code:
            print("Code faux: il vous reste {} tentatives".format(3-self.__nTentatives))
            
        elif self.__nTentatives > 3:
            print("code faux: Il ne vous reste plus de tentatives ")
            self.__nTentatives  = 3
                  
        
    def __str__(self):
        return "A({}, {})".format(self.__val, self.__nTentatives)
    
    
choix = 1

val, code = -3, 2 
newVal = 4
testCode = -10

valCode = (newVal,testCode)
#print(valCode)

myObj = A(val,code)

myObj.val = valCode
print(myObj)

myObj.val = (4,6)
print(myObj)

myObj.val = (4,2)
print(myObj)



