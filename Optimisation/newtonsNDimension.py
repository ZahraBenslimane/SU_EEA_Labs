# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:35:45 2021

@author: zahra
"""

#%% Import des librairies
import numpy as np 
import matplotlib.pyplot as plt

#%% Définitions des fonctions


def newtonsNDimension (J, gradJ, HJ, X0, epsilon, nMax):
    tab_XN = [ X0 ]
    XN0 = X0
    dX = 1
    n  = 0
    
    converge = False
    minimum = False
    maximum = False
    pointSelle = False
    
    while abs(dX) > epsilon and n <= nMax:
        
        gradX1, gradX2 = gradJ(XN0[0], XN0[1])
        GJ = np.array([gradX1,gradX2])
        HJ = hessJ(XN0[0], XN0[1])
       
        delta_X = np.linalg.solve(HJ ,-GJ)
        XN0 = XN0 + delta_X
        dX =  np.linalg.norm(delta_X)
        
        #print(XN0)
        
        tab_XN.append( XN0 )
        n += 1
    if abs(dX) <= epsilon :
        converge = True
        HJ = hessJ(XN0[0], XN0[1])
        #print(HJ)
        #print("\nDeterminant de la hessienne du point de convergance det(HJ(x1,x2)) = ", np.linalg.det(HJ))
        eigenValues = np.linalg.eigvals(HJ)
        #print("valeurs propres : ", np.linalg.eigvals(HJ) )
        if eigenValues[0] > 0  and eigenValues[1] > 0:
            minimum = True
        elif eigenValues[0] < 0  and eigenValues[1] < 0:
            maximum = True
        elif eigenValues[0] * eigenValues[1] < 0:
            pointSelle = True
        else: 
            print("Error : On ne peut rien conclure sur ce point de convergance : une des valeurs propres est nulle")      
        
        
    tab_XN = np.array( tab_XN )
    return tab_XN, converge, n, minimum, maximum, pointSelle

#%%
def J(x1,x2):
    return x1**2 + 1.5 * x2**2 - 5*np.sin(2*x1 + x2) + 5*np.sin(x1 - x2)

def gradJ(x1, x2):
    gradX1 = 2*x1 - 5*2*np.cos(2*x1 + x2) + 5*np.cos(x1 - x2)
    gradX2 = 2*1.5*x2 - 5*np.cos(2*x1 + x2) - 5*np.cos(x1 - x2)
    return gradX1, gradX2

def hessJ(x1, x2):
    Dx1Dx1 = 2 + 20*np.sin(2*x1 + x2) - 5*np.sin(x1 - x2)
    Dx1Dx2 = 10*np.sin(2*x1 + x2) + 5*np.sin(x1 - x2)
    Dx2Dx1 = 10*np.sin(2*x1 + x2) + 5*np.sin(x1 - x2)
    Dx2Dx2 = 3 + 5*np.sin(2*x1 + x2) - 5*np.sin(x1 - x2)
    return np.matrix([[Dx1Dx1, Dx1Dx2 ], [Dx2Dx1, Dx2Dx2 ]])

#%%

nb_pointsAléatoires = 40
cpt_point_convergant = 0

import random
randomlist_x1 = []
randomlist_x2 = []
for i in range(0,nb_pointsAléatoires):
    n1 = random.uniform(-4,4)
    n2 = random.uniform(-4,4)    
    randomlist_x1.append(n1)
    randomlist_x2.append(n2)
  
fig = plt.figure( figsize=(12, 12))

# Discrétisation du domaine de tracé
tab_x1  = np.linspace(-4,4,201)
tab_x2  = np.linspace(-4,4,201)
x1_2D, x2_2D = np.meshgrid(tab_x1, tab_x2)
# Tracé des isovaleurs 
nIso = 50
plt.contour(x1_2D, x2_2D, J(x1_2D, x2_2D), nIso)
plt.title('Isovaleurs')
plt.xlabel('Valeurs de x1')
plt.ylabel('Valeurs de x2')
plt.grid()
plt.axis('square')
    
for i in range(nb_pointsAléatoires) : 

    XN, converge , n , minimum, maximum, pointSelle = newtonsNDimension(J, gradJ, hessJ, np.array([randomlist_x1[i],randomlist_x2[i]]), 1e-1, 10)
    
    
    #print(XN)
    if converge == True :
        cpt_point_convergant += 1
        print("Point de départ : x0 = {:.4f} , {:.4f}".format( randomlist_x1[i]  , randomlist_x2[i]) )
        if minimum == True:
            print("Convergeance vers un MINIMUM LOCAL \nxMIN = {}, après : {} itérations\n".format(XN[-1,:], n))
        if maximum == True:
            print("Convergeance vers un MAXIMUM LOCAL \nxMAX = {}, après : {} itérations\n".format(XN[-1,:], n))
        if pointSelle == True:
            print("Convergeance vers un POINT SELLE \nx = {}, après : {} itérations\n".format(XN[-1,:], n)) 
            
        
    else:
        print("Point de départ : x0 = {:.4f} , {:.4f}".format( randomlist_x1[i] , randomlist_x2[i]) )
        print("Divergeance !\n")
        
    # Tracé des segments
    x1_values = np.array(XN[:,0])
    x2_values = np.array(XN[:,1])
    plt.plot(x1_values, x2_values, 'c')
    # Tracés des points de départs et d'arrivés
    plt.plot( XN[0][0],XN[0][1],'bs', label = 'xN')
    if (minimum == True):
        plt.plot( XN[-1][0],XN[-1][1],'rs', label = 'xmin')
    if (maximum == True):
        plt.plot( XN[-1][0],XN[-1][1],'gs', label = 'xmax')
    if (pointSelle == True):
        plt.plot( XN[-1][0],XN[-1][1],'ms', label = 'x_pointselle')

print("La méthode de newton à converger {} fois /{} points de départs aléatoires".format(cpt_point_convergant, nb_pointsAléatoires))    
            

#x0 = 2.5676 , 1.7128
