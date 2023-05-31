#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 17:45:55 2021

@author: benaissa
"""

# Exo1 : Polynome

# p = [a0 a1 a2 ..... an]

def getValeur(p,x):
    val = 0
    for i in range(len(p)):
        val+= p[i]* x**i
    return val

def getDerivee(p,x):
    der = 0
    for i in range(1,len(p)):
        der+= i* p[i]* x**(i-1)
    return der
        
# main pour le test du bon fonctionnement :
p1 = [1 ,2 ,2]
p2 = [3, 5 ,1]

print(getValeur(p1,1)) # 5
print(getValeur(p2,5)) # 53

print(getDerivee(p1,2)) #10
print(getDerivee(p2,3)) #11

# il marche bien


# Exo 2 :

def dichotomie (p,a,b,eps):
    pA = getValeur(p,a)
    pB = getValeur(p,b)
    c = (a+b)/2
    pC = getValeur(p,c)
    if pA == 0:
        return a
    elif pB == 0:
        return b
    else : 
        while (abs(b-a) > eps and pC != 0):
            c = (a+b)/2
            pC = getValeur(p,c)
            
            if pA*pC <0 :
                b = c
                pB = pC
            else :
                a = c
                pA = pC
                
        return c

ptest = [-6, -1, 1] # recherche racine 3
sol_dic = dichotomie(ptest,2,4,0.001)
print(sol_dic)

# ça marche

def newton (p,x0,eps):
    uN = eps +1
    while (getValeur(p,x0) != 0) and (abs(uN) > eps):
        uN = getValeur(p,x0)/getDerivee(p,x0)
        x0 = x0 - uN
        
    return x0

sol_new = newton(ptest,2.5,0.001)
print(sol_new)

# test avec l'exemple donné
p0 = [0.8571, -0.0714, -0.9286, 0.0714, 0.0714]

sol0_d = dichotomie(p0,2,4,1e-5)
Sol0_n = newton(p0,2,1e-5)
print("solution avec dichotomoie ", sol0_d)
print("solution avec newton ",Sol0_n )


# Exo 3 :
    
    #Polynome :

        
        
def afficherPoly(p):
    n = len(p)
    res = ""
    for i in range(n-1,0,-1):
        if p[i] >= 0  and i != n-1:     
            res += " + "   
        res += " "+ str(p[i])+" x^"+str(i)
    if p[0] >= 0:
        res += " + "   
    res += str(p[0])
    
    print(res)

afficherPoly(p0)         # ça marche bien

def EgalPoly (p1,p2) :
    n1 = len(p1)
    n2 = len(p2)
    if (n1 == n2):
        
        for i in range(n1):
            
            if p1[i] != p2[i]:
                
                print("ils sont pas egaux")
                return False
            
            
        print("ils sont égaux")
        return True
    else: 
        
         
     
         nmin = min (n1,n2)
         nmax = max(n1,n2)
         
         for i in range(nmin):
             
             if p1[i] != p2[i]:
                 
                 print("ils sont pas egaux")
                 return False
             
         p = p1
         
         if n2 > n1 :
             p = p2
         for i in range(nmin+1,nmax):
             if p[i] != 0:
                 print("ils sont pas egaux")
                 return False
            
         print("ils sont egaux")
         return True
print("----------------")
afficherPoly(ptest)
afficherPoly(p0)            
EgalPoly(ptest, p0) 
  
EgalPoly(p0, p0)   
  
pm = [ 0, 0.8571, -0.0714, -0.9286, 0.0714, 0.0714]  

afficherPoly(pm)
afficherPoly(p0)

EgalPoly(pm, p0)   

pn = [ 1, 0.8571, -0.0714, -0.9286, 0.0714, 0.0714]
afficherPoly(pn)
afficherPoly(p0)
EgalPoly(pn, p0)    # marche tres bien

# Comment gérer le cas ou il y'a pas une racine dans R  ??
