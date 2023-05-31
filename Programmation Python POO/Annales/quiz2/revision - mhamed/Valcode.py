#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 01:40:13 2021

@author: benaissa
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
            
        elif 3 >= self.__nTentatives > 0 and code != self.__code:
            print("Code faux: il vous reste {} tentatives.".format(3-self.__nTentatives))
            
        elif self.__nTentatives > 3:
            print("Nombre de tentatives depasse: modification impossible")
            self.__nTentatives  = 3
                  
        
    def __str__(self):
        return "A({}, {})".format(self.__val, self.__nTentatives)
    
    