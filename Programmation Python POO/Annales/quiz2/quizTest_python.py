# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 07:21:39 2021

@author: zahra
"""

def quelleSaison( mois ) :
    if 1 <= mois <= 3:
        return "Hiver"
    if 4 <= mois <= 6:
        return "Printemps"
    if 7 <= mois <= 9:
        return "Ete"
    if 10 <= mois <= 12:
        return "Automne"
    else:
        return "Erreur"
    
def afficherPyramide( n ) :
    for i in range(n+1):
        print( " "*i + "*"*( 2*(n-i) - 1) )
        
        
def sommeTab( tab1, tab2 ) :
    res = []
    if len(tab1) < len(tab2):
        size = len(tab1)
    elif len(tab1) > len(tab2) :
        size = len(tab2)
    else :
        size = len(tab2) 
    
    for i in range(size):
        res.append(tab1[i] + tab2[i])
        
    if len(tab1) < len(tab2):
        res.extend( tab2[i+1:] )
    else :
        res.extend( tab1[i+1:] )
    return res

def isTrie( tab ) :
    #print(tab)
    if all(tab[j] == tab[j+1] for j in range(len(tab)-1)):
        return("Tous les elements egaux")
    elif all(tab[j] <= tab[j+1] for j in range(len(tab)-1)):
        return("Tri croissant")
    elif all(tab[j] >= tab[j+1] for j in range(len(tab)-1)):
        return("Tri decroissant")
    else :
        return("Non trie")
    
def gravite( grille ) :
    for i in range(len(grille)-2 ,-1, -1):
        for j in range(len(grille[0])):
            if grille[i][j] == '#' : 
                for index in range(i+1, len(grille), +1):
                    if  grille[index][j] == ' ':
                        grille[index][j] = '#'
                        grille[index-1][j] = ' '
                        #print(np.matrix(grille))

                
                
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

def isSecuOk( sSecu ):
    num = sSecu.split()
    #print(num)
    sexe = int(num[0])
    annee_naissance =  int(num[1])
    mois_naissance =  int(num[2])
    departement_naissance = int(num[3]) 
    comune_naissance =  int(num[4])
    numero_naissance = int(num[5])
    cle = int(num[6])
    NIR = int (num[0] + num[1] + num[2]+ num[3] + num[4] + num[5])
    
    #print("nir = ", NIR)
    if  sexe < 1 or  sexe > 2:
        return "Erreur: Sexe incorrect"
    if annee_naissance > 2021:
        return "Erreur: Annee de naissance incorrect"
    if mois_naissance>12 or  mois_naissance < 1:
        return "Erreur: Mois de naissance incorrect"
    if departement_naissance>97 or departement_naissance < 1 :
        return "Erreur: Departement de naissance incorrect"
    if comune_naissance> 999 or comune_naissance <1:
        return "Erreur: Commune de naissance incorrect"
    if numero_naissance> 999 or numero_naissance <1:
        return "Erreur: Numero de naissance incorrect"
    if cle != 97 - (NIR%97):
        return "Numero de securite sociale incorrect"
        
    else :
        return "Numero de securite sociale correct"
    



