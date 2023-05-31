#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 22:17:13 2021

@author: benaissa
"""
# Partie Exo 1
class Polynome:
    def __init__(self, coefficients):
        self.__coefficients = coefficients
    def __str__(self):
        n = len(self.coefficients)
        res = ""
        for i in range(n-1,0,-1):
            if self.coefficients[i] >= 0  and i != n-1:     
                res += " + "   
            res += " "+ str(self.coefficients[i])+" x^"+str(i)
        if self.coefficients[0] >= 0:
            res += " + "   
        res += str(self.coefficients[0])
        return res
    
    def getDegree(self):
        n = len(self.coefficients)
        if self.coefficients[n-1] != 0: #   aa confirmer
            return n-1
        
        else : 
            n = n-1
            while( self.coefficients[n] == 0):
                n = n-1
            return n
    def getValeur(self,x):
        val = 0
        for i in range(len(self.coefficients)):
            val+= self.coefficients[i]* x**i
        return val
        
    def getDerivee(self,x):
        der = 0
        for i in range(1,len(self.coefficients)):
            der+= i* self.coefficients[i]* x**(i-1)
        return der
    
    def __eq__(self,other):
        if not isinstance(other,Polynome):
            return False
        if self is other:
            return True
        
        n1 = len(self.coefficients)
        n2 = len(other.coefficients)
        if (n1 == n2):   
            for i in range(n1): 
                if self.coefficients[i] != other.coefficients[i]:
                    return False
            return True
        else: 
             nmin = min (n1,n2)
             nmax = max(n1,n2)
             for i in range(nmin):  
                 if self.coefficients[i] != other.coefficients[i]:
                     return False
                 
             p = self.coefficients
             
             if n2 > n1 :
                 p = other.coefficients
             for i in range(nmin+1,nmax):
                 if p[i] != 0:
                     return False
             return True
    def __add__(self,other):
        
        n1 = len(self.coefficients) 
        n2 = len(other.coefficients)
        nmin = min (n1,n2)
        nmax = max(n1,n2)
        coeff = [0 for i in range(nmax)]
        p = self.coefficients
        if n2 > n1 :
            p = other.coefficients
        for i in range (nmin):
            coeff[i] = self.coefficients[i] + other.coefficients[i] 
        for i in range(nmin+1,nmax):
            coeff[i] = p[i] 
        return Polynome(coeff)
    
    
    @property   # getter
    def coefficients(self):
        return self.__coefficients 
    @coefficients.setter
    def coefficients(self,coefficients):
        self.__coefficients = coefficients
    
# Parttie Exo 2 : 
    
class Solveur:
    def __init__(self,p,precision):
        self.__p = p
        self.__precision = precision
     
    @property
    def p(self):
        return self.__p
    @p.setter
    def p(self,p):
        self.__p= p
    @property 
    def precision(self):
        return self.__precision 
    @precision.setter
    def precision(self,precision):
        self.__precision = precision
    
    
    def newton(self, x0):
        uN = self.precision +1
        while (self.p.getValeur(x0) != 0) and (abs(uN) > self.precision):
            uN = self.p.getValeur(x0)/self.p.getDerivee(x0)
            x0 = x0 - uN    
        return x0
    def dichotomie(self,a,b):
        pA = self.p.getValeur(a)
        pB = self.p.getValeur(b)
        c = (a+b)/2
        pC = self.p.getValeur(c)
        if pA == 0:
            return a
        elif pB == 0:
            return b
        else : 
            while (abs(b-a) > self.precision and pC != 0):
                c = (a+b)/2
                pC = self.p.getValeur(c)
                if pA*pC <0 :
                    b = c
                    pB = pC
                else :
                    a = c
                    pA = pC    
            return c
        
    
# main
# Partie Exo 1
print("test des cas exceptionnel")
coef1 = [1, -1, -1]
p1 = Polynome(coef1)
print(p1)
print("degré",p1.getDegree())
print("test demandé")
coef0 = [0.8571, -0.0714, -0.9286, 0.0714, 0.0714]

p0 = Polynome(coef0)
print(p0)
print("degré",p0.getDegree())

print("p0(0) = ", p0.getValeur(0))
print("p0(1) = ", p0.getValeur(1))
print("p0(2) = ", p0.getValeur(2))

print("p0'(0) = ", p0.getDerivee(0))
print("p0'(1) = ", p0.getDerivee(1))
print("p0'(2) = ", p0.getDerivee(2))
        
print("test de la fonction add")
print(p1+p0)

# Partie Exo 2

print("test des solveurs")
Solv1 = Solveur(p1,1e-5)
print("solution avec Newton :")
print(Solv1.newton(2))
print("solution avec la methode dichotomie")
print(Solv1.dichotomie(0,5))

print("-----------------------")

pc = [-6, -1, 1]
print("test des solveurs sur le polynome suivant :")
ptest = Polynome(pc)
print(ptest)
Solv2 = Solveur(ptest,1e-5)
print("solution avec Newton :")
print(Solv2.newton(2))
print("solution avec la methode dichotomie")
print(Solv2.dichotomie(0,5))



