# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 12:27:42 2021

@author: zahra
"""

#%% Import des librairies
import numpy as np 
import matplotlib.pyplot as plt
import random

#%% Méthodes de calculs

######################### Descente en gradient #############################

def fixedStepGradient(J, gradJ, X0, alpha, epsilon, nMax ):
    tab_XN = np.array([[X0[0], X0[1]]])
    x1, x2 = X0[0], X0[1]
    dX = 1
    n  = 0
    converge = True

    while abs(dX) > epsilon and n <= nMax:
        
        gradX1, gradX2 = gradJ(x1, x2)
        xN1 = x1 - alpha*gradX1
        xN2 = x2 - alpha*gradX2
        dX = np.sqrt((xN1 - x1)**2 + (xN2 - x2)**2 )

        tab_XN = np.append( tab_XN, [ [x1, x2] ]  , axis = 0)
        x1, x2 = xN1, xN2
        n += 1
        
    if abs(dX) >= epsilon :
        converge = False
    return tab_XN, converge, n

def AdaptativeGradient(J, gradJ, X0, alpha, epsilon, nMax ):
    tab_XN = np.array([[X0[0], X0[1]]])
    x1, x2 = X0[0], X0[1]
    dX = 1
    n  = 0
    converge = True
    
    alphaUpdates = [alpha]  #garder tous les alpha pour graphic

    while abs(dX) > epsilon and n <= nMax:
        
        gradX1, gradX2 = gradJ(x1, x2)
        xN1 = x1 - alpha*gradX1
        xN2 = x2 - alpha*gradX2
        dX = np.sqrt((xN1 - x1)**2 + (xN2 - x2)**2 )
        #print(dX)
        
        while J(xN1, xN2) > J(x1, x2):
            alpha = alpha/2
            # Regarder si on peut y allez encore plus vite
            xN1 = x1 - alpha*gradX1
            xN2 = x2 - alpha*gradX2
                
        alpha = alpha * 2
 
        alphaUpdates.append(alpha)
        x1, x2 = xN1, xN2
        tab_XN = np.append( tab_XN, [ [x1, x2] ]  , axis = 0)
        n += 1
        
    if abs(dX) >= epsilon :
        converge = False
        
    alphaUpdates = np.array(alphaUpdates)
    
    return tab_XN, converge, n, alphaUpdates

#############################    NEWTON     #############################

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


#%% Fonctions Tests : Fonction + gradient + Hessienne
    
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


#%% Fonctions D'affichage
def afficher_AdaptativeGradient(nb_pointsAléatoires,tab_alpha_zéro):
    # Génération de nb_pointsAléatoires aléatoire pour le test de la fonction
    randomlist_x1 = []
    randomlist_x2 = []
    for i in range(0,nb_pointsAléatoires):
        n1 = random.uniform(-4,4)
        n2 = random.uniform(-4,4)    
        randomlist_x1.append(n1)
        randomlist_x2.append(n2)
    
    fig2 = plt.figure( figsize=(8, 6)) 
     
    fig = plt.figure( figsize=(8,9))
       
    for j in range(len(tab_alpha_zéro)):
         
        axi = fig.add_subplot(2,2, j+1)
        fig.suptitle('Isovaleurs' , fontsize=20)
        
        #% Tracé des isovaleurs de J
        # Discrétisation du domaine de tracé
        tab_x1  = np.linspace(-4,4,101)
        tab_x2  = np.linspace(-4,4,101)
        x1_2D, x2_2D = np.meshgrid(tab_x1, tab_x2)  
        # Tracé des isovaleurs 
        nIso = 40
        axi.contour(x1_2D, x2_2D, J(x1_2D, x2_2D), nIso)
        plt.title("Alpha = {} ".format( tab_alpha_zéro[j] ))
        plt.xlabel('Valeurs de x1')
        plt.ylabel('Valeurs de x2')
        plt.grid()
        plt.axis('square')
        cpt_point_convergant = 0
        
        axi2 = fig2.add_subplot(2,2, j+1)   #for alpha
        fig2.suptitle('Evolution de alpha au cours des itérations' , fontsize=20)
        axi2.set_title("Alpha_zéro = {} ".format( tab_alpha_zéro[j] ))
    
        print("---------------   Calcul pour alpha = {}  ------------------".format(tab_alpha_zéro[j]))
        for i in range(nb_pointsAléatoires) :  
              
            XN, converge , n ,alphaUpdates = AdaptativeGradient(J, gradJ, [randomlist_x1[i],randomlist_x2[i]], tab_alpha_zéro[j], 1e-3, 1000)
    
            if converge == True:
                cpt_point_convergant += 1
                #print("Point de départ : x0 = {:.4f} , {:.4f}".format( randomlist_x1[i] , randomlist_x2[i]) )
                #print("Convergeance vers xmin = {}, après : {} itérations\n".format(XN[-1,:], n))
            '''
            else:
                print("Point de départ : x0 = {:.4f} , {:.4f}".format( randomlist_x1[i] , randomlist_x2[i]) )
                print("Divergeance !\n")
            '''        
            # Tracé des segments
            x1_values = np.array(XN[:,0])
            x2_values = np.array(XN[:,1])
            axi.plot(x1_values, x2_values,'m', linewidth=2)
            # Tracé des points de départs et d'arrivé
            axi.plot( XN[-1][0],XN[-1][1],'rs',linewidth=7, label = 'x0')
            axi.plot( XN[0][0],XN[0][1],'bs',linewidth=7, label = 'xN')
            
            # Tracé de l'évolution d'alpha au cours des itérations pour le premier point aléatoir
            if i == 1:
                #tab_n = np.arange(1, cpt_changer_alpha + 2)
                tab_n = np.arange(1, n + 2)
                axi2.plot(tab_n, alphaUpdates,'r-', linewidth=2)
                    
        print("Gradient Descent  à converger {} fois /{} points de départs aléatoires\n".format(cpt_point_convergant, nb_pointsAléatoires))
                
#%%   
        
def mixedSolution(J, gradJ, HJ, X0,alpha, epsilon1, epsilon2, nMax1, nMax2): 
    tab_XN1, converge, n1, alphaUpdates =  AdaptativeGradient(J, gradJ, X0, alpha, epsilon1, nMax1 )
    X0_prime = np.array ([ tab_XN1[-1][0] , tab_XN1[-1][1] ])
    tab_XN2, converge , n2 , minimum, maximum, pointSelle = newtonsNDimension(J, gradJ, hessJ, X0_prime , epsilon2, nMax2)    
    tab_XN = np.concatenate((tab_XN1, tab_XN2))
    return tab_XN,converge, n1+n2, minimum, maximum, pointSelle


nb_pointsAléatoires = 5
def afficher_solutionMixte(nb_pointsAléatoires, alpha, epsilon1, epsilon2, nMax1, nMax2):
    cpt_point_convergant_newton = 0
    cpt_minimum = 0
    cpt_maximum = 0
    cpt_pointSelle = 0
    
    randomlist_x1 = []
    randomlist_x2 = []
    for i in range(0,nb_pointsAléatoires):
        n1 = random.uniform(-4,4)
        n2 = random.uniform(-4,4)    
        randomlist_x1.append(n1)
        randomlist_x2.append(n2)
        
    fig = plt.figure( figsize=(6, 6))
    
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
    
        XN,converge,n, minimum, maximum, pointSelle = mixedSolution(J, gradJ, hessJ, np.array([randomlist_x1[i],randomlist_x2[i]]),alpha,epsilon1, epsilon2, nMax1, nMax2)
        if converge == True :
            cpt_point_convergant_newton += 1 
        # Tracé des segments
        x1_values = np.array(XN[:,0])
        x2_values = np.array(XN[:,1])
        plt.plot(x1_values, x2_values, 'c')
        # Tracés des points de départs et d'arrivés
        plt.plot( XN[0][0],XN[0][1],'bs', label = 'xN')
        if (minimum == True):
            plt.plot( XN[-1][0],XN[-1][1],'rs', label = 'xmin')
            cpt_minimum+=1
        if (maximum == True):
            plt.plot( XN[-1][0],XN[-1][1],'gs', label = 'xmax')
            cpt_maximum+=1
        if (pointSelle == True):
            plt.plot( XN[-1][0],XN[-1][1],'ms', label = 'x_pointselle')
            cpt_pointSelle+=1
    
    print("La méthode de newton à converger {} fois /{} points de départs aléatoires".format(cpt_point_convergant_newton, nb_pointsAléatoires))    
    print("Le nombre de minimum local trouvés = {}".format(cpt_minimum))   
    print("Le nombre de maximum local trouvés = {}".format(cpt_maximum)) 
    print("Le nombre de points selles trouvés = {}".format(cpt_pointSelle))             
    
   
#afficher_solutionMixte(80)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      

