# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:24:28 2021

@author: zahra
"""

import numpy as np 

def sommeTab( tab1, tab2 ) :
    res = []
    
    if len(tab1) < len(tab2):
        size = len(tab1)
    elif len(tab1) > len(tab2) :
        size = len(tab2)
    else :
        size = len(tab2) 
    print(size) 
    
    for i in range(size):
        res.append(tab1[i] + tab2[i])
        
    if len(tab1) < len(tab2):
        res.extend( tab2[i+1:] )
    else :
        res.extend( tab1[i+1:] )
    return res
        
tab1 = [1,1,1,1]
tab2 = [1,1,1,1,5,6]

#print( sommeTab( tab1, tab2 ) )

def gravite( grille ) :
    for i in range(len(grille)-2 ,-1, -1):
        for j in range(len(grille[0])):
            if grille[i][j] == '#' : 
                for index in range(i+1, len(grille), +1):
                    if  grille[index][j] == ' ':
                        grille[index][j] = '#'
                        grille[index-1][j] = ' '
                        #print(np.matrix(grille))
    
    


#grille = [ [ ' ', '#', '#', ' ' ],  [ ' ', '#', ' ', ' ' ], [ '#', ' ', '#', '#' ],  [ ' ', ' ', ' ', '#' ] ]

grille = [ [ ' ', '#', '#', ' ' ], \
           [ ' ', '#', ' ', ' ' ], \
           [ '#', ' ', '#', '#' ], \
           [ ' ', ' ', ' ', '#' ] ]


'''
gravite(grille)
print("\n")
print(np.matrix(grille))
'''


def afficherMots( phrase ) :
    for i,letter in enumerate(phrase) :
        if letter.isalnum() :
            print(letter, end ='')
        elif  phrase[i-1].isalnum() :
            print("")
            
        
	

def getAge( date1, date2 ) :
    date1 = date1.split("/")
    date2 = date2.split("/")   
    
    annee1 = int( date1[2] )
    annee2 = int( date2[2] )
    
    if annee2 > annee1:
        res = annee2 - annee1
    elif annee2 < annee1:
        annee1 - annee2
    else :
        res = 0
    return res
        



mot = "Vive Charlie et les 42 loutres!"
mot2 = "Vive  Charlie-_'(&)@ et les 42 loutres!!!!!!!!!!!!"


#afficherMots( mot ) 

date1, date2 = "12/07/1998", "15/07/2018"
#print(getAge(date1, date2))


def isSecuOk( sSecu ):
    
    for i in range(len(sSecu)):
        
        num = sSecu[i].split()
        print(len(num))
        print(num[6])
        sexe = int(num[0])
        annee_naissance =  int(num[1])
        mois_naissance =  int(num[2])
        departement_naissance = int(num[3]) 
        comune_naissance =  int(num[4])
        numero_naissance = int(num[5])
        cle = int(num[6])
        
        NIR = sexe + annee_naissance + mois_naissance + departement_naissance + comune_naissance +  numero_naissance
        
        
        if 1 > sexe > 2:
            return "Erreur: Sexe incorrect"
        elif annee_naissance > 2021:
            return "Erreur: Annee de naissance incorrect"
        elif 1>mois_naissance>12:
            return "Erreur: Mois de naissance incorrect"
        elif 1>departement_naissance>97:
            return "Erreur: Departement de naissance incorrect"
        elif 1> comune_naissance> 999:
            return "Erreur: Commune de naissance incorrect"
        elif 1> numero_naissance> 999:
            return "Erreur: Numero de naissance incorrect"
        elif cle != 97 - (NIR%97):
            return "Numero de securite sociale incorrect"
        else :
            return "Numero de securite sociale correct"
            
            
        
            

    





sSecus = [ '2 85 10 23 363 118 77', '3 61 02 85 775 310 41',
           '1 71 13 19 244 981 87', '2 64 09 23 027 000 36',
           '1 68 04 89 297 191 32']

isSecuOk( sSecus )










