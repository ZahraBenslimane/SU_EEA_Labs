# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 15:26:04 2021

@author: zahra
"""

#%% Import des librairies
import numpy as np 
import matplotlib.pyplot as plt
import random

import newtonsNDimension

#%% Définitions des fonctions

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


#%% Fonctions Tests :
    
def J(x1,x2):
    return x1**2 + 1.5 * x2**2 - 5*np.sin(2*x1 + x2) + 5*np.sin(x1 - x2)

def gradJ(x1, x2):
    gradX1 = 2*x1 - 5*2*np.cos(2*x1 + x2) + 5*np.cos(x1 - x2)
    gradX2 = 2*1.5*x2 - 5*np.cos(2*x1 + x2) - 5*np.cos(x1 - x2)
    return gradX1, gradX2

#%% Tracé des isovaleurs de J et les segment pour un seul point 
'''
X0 = [0,3]

XN, converge , n = fixedStepGradient(J, gradJ, X0 , 0.071, 1e-3, 1000)

if converge == True :
    print("Point de départ : x0 = {:.4f} , {:.4f}".format( X0[0] , X0[1] ) )
    print("Convergance aprés {} itérations : xMIN = {} \n".format( n, XN[-1,:]))   
    
else:
    print("Point de départ : x0 = {:.4f} , {:.4f}".format( X0[0] , X0[1] ) )
    print("Divergeance !\n")

fig = plt.figure(figsize=(13, 13))
ax1 = fig.add_subplot(121)

# Discrétisation du domaine de tracé
tab_x1  = np.linspace(-4,4,101)
tab_x2  = np.linspace(-4,4,101)
x1_2D, x2_2D = np.meshgrid(tab_x1, tab_x2)

# Tracé des isovaleurs 
nIso = 50
ax1.contour(x1_2D, x2_2D, J(x1_2D, x2_2D), nIso)
plt.title('Isovaleurs')
plt.xlabel('Valeurs de x1')
plt.ylabel('Valeurs de x2')
plt.grid()
ax1.axis('square')

# Tracé des segments
x1_values = np.array(XN[:,0])
x2_values = np.array(XN[:,1])
plt.plot(x1_values, x2_values)

# Tracé des points de départs et d'arrivés
plt.plot( XN[-1][0],XN[-1][1],'rs', label = 'x0')
plt.plot( XN[0][0],XN[0][1],'bs', label = 'xN')

ax2 = fig.add_subplot(122, projection = '3d')
ax2.contour3D(x1_2D, x2_2D, J(x1_2D, x2_2D) ,80 )
ax2.plot(XN[:,0],XN[:,1],J(XN[:,0], XN[:,1]), c ='r', marker='o',linewidth=1 )



'''
#%% Tester l’algorithme pour différente valeurs de 𝛼 et différents points de départ

'''
# Génération de nb_pointsAléatoires aléatoire pour le test de la fonction
randomlist_x1 = []
randomlist_x2 = []
for i in range(0,nb_pointsAléatoires):
    n1 = random.uniform(-4,4)
    n2 = random.uniform(-4,4)    
    randomlist_x1.append(n1)
    randomlist_x2.append(n2)

fig2 = plt.figure( figsize=(10, 10)) 
 
fig = plt.figure( figsize=(10, 10))
   
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
        
        #else:
            #print("Point de départ : x0 = {:.4f} , {:.4f}".format( randomlist_x1[i] , randomlist_x2[i]) )
            #print("Divergeance !\n")
                
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


'''        
#%% Tracé de l'évolution d'alpha au cours des itérations : différente valeurs de 𝛼 et différents points de départ

def afficher_AdaptativeGradient(nb_pointsAléatoires,tab_alpha_zéro):
    # Génération de nb_pointsAléatoires aléatoire pour le test de la fonction
    randomlist_x1 = []
    randomlist_x2 = []
    for i in range(0,nb_pointsAléatoires):
        n1 = random.uniform(-4,4)
        n2 = random.uniform(-4,4)    
        randomlist_x1.append(n1)
        randomlist_x2.append(n2)
    
    fig2 = plt.figure( figsize=(7, 7)) 
     
    fig = plt.figure( figsize=(7, 7))
       
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
                
nb_pointsAléatoires = 80
tab_alpha_zéro = np.linspace(0.04,0.09,4)

#afficher_AdaptativeGradient(nb_pointsAléatoires,tab_alpha_zéro)


 
    












    



