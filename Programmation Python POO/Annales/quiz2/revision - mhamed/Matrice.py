#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 12:11:01 2021

@author: benaissa
"""

# MAtrice

class Matrice :
    def __init__(self,coeffs): 
        if type(coeff[0][0]) == int : #  integer
            self.coeffs = coeffs 
        if type(coeff[0][0]) == str : # string
            self.coeffs = coeffs 
    
            
            
    def __str__(self):
        res = ""
        m = len(self.coeffs)
        n = len(self.coeffs[1])
        for i in range(m):
            for j in range(n):
                res += "| " 
                if  type(self.coeffs[i][j]) == str:
                    res += self.coeffs[i][j] + " "
                elif type(self.coeffs[i][j]) == int:
                    res += str(self.coeffs[i][j]) + " " 
            res += "|\n"
        return res
            
    
    
    # m = len(self.coeffs)
    # n = len(self.coeffs[1])
    # for i in range(m):
    #     for j in range(n):
    #         print("| ", end= "")
    #         print(self.coeffs[i][j], end = " ")
    #     print("|")
        
        
 
            
 
    
coeff = [ [3,2,1],[4,6,4]]
M = Matrice(coeff)
print(M)

coeff1 = [["3","2","1"],["4","6","4"]]
M1 = Matrice(coeff1)
print(M1)

