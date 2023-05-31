import tkinter as tk
from tkinter import ttk
from GuiElementFonction import createGuiElementFonction, createGuiElementGraph, createGuiElementSolver
#from fonction import Polynome, Sinus, Exponentielle, SommeFonction, Solveur

from Polynome import Polynome
from Sinus import Sinus
from Exponentielle import Exponentielle
from SommeFonction import SommeFonction
from Solveur import Solveur


class FonctionSolveur (tk.Frame) :
    __sizeGraph = [ 500, 500 ]      # Taille du graphique
    __geFonction = createGuiElementFonction( )
    __geGraph = createGuiElementGraph( )
    __geSolver = createGuiElementSolver( )
    __rbSolver = { "Dichotomie" : "1", "Newton" : "2" }
    
    def __init__(self, master = None) :
        # Fenetre graphique
        super( ).__init__( master )
        self.master = master        
        self.master.title( "Solveur de fonctions" )
        self.master.geometry( "800x510" )   # Taille de la fenetre
        # Panneau gauche
        frame = tk.Frame( self.master, relief = "groove" )
        self.createFonctionPanel( frame )   # Parametres des fonctions
        self.createSolverPanel( frame )     # Solveur et gestion du graphique
        self.__txtLog = tk.Text( frame, state = "normal", height = 12, width = 40 ) # Zone de texte
        self.__txtLog.bind("<Key>", lambda a: "break")  # Desactive le clavier pour le log
        self.__txtLog.pack( )
        frame.pack( side = "left" )
        # Panneau de droite
        self.createDrawPanel( )     # Graphique
        self.pack( )
        # On cree une fonction nulle et une liste vide de fonctions
        self.__fcn = None
        self.__fcnList = [ ]
        # On trace le repere
        self.draw( )
        

    # =============================================================================
    #     Fonctions de creation des differents elements de l'interface
    # =============================================================================
    def createFonctionPanel( self, frame ) :
        subFrame = tk.LabelFrame( frame, text = "Gestion des fonctions" )
        # On ajoute les onglets de gestion des parametres de fonction
        self.__nbFonction = self.createParamPanel( subFrame )
            # On ajoute les boutons (pour ajouter, supprimer ou afficher)
        self.__btnAdd = tk.Button( subFrame, text = "Ajouter", command = self.ajouterFonction )
        self.__btnAdd.grid( row = 1, column = 0, padx = 1, pady = 1 )
        self.__btnDel = tk.Button( subFrame, text = "Supprimer", command = self.supprimerFonction, state = "disabled" )
        self.__btnDel.grid( row = 1, column = 1, padx = 1, pady = 1 )
        self.__btnPrint = tk.Button( subFrame, text = "Afficher", command = self.afficherFonction, state = "disabled" )
        self.__btnPrint.grid( row = 1, column = 2, padx = 1, pady = 1 )
            # On ajoute la liste deroulante
        self.__cboxFcn = ttk.Combobox( subFrame, values = [ ], state = "disabled" )
        self.__cboxFcn.grid( column = 0, columnspan = 3 )
        
        subFrame.pack( )
        
    def createParamPanel( self, frame ) :
        """
            Creer le notebook et les onglets pour chaque type de fonctions
            Chaque onglet permet de saisir les differents parametres de la fonction
            @param frame le panel general ou les onglets doivent etre integres
        """
        subFrame = ttk.Notebook( frame )
        self.__editsFonction, self.__tabFonction = [ ], [ ]
        for i, ge in enumerate( self.__geFonction ) :
            # On cree un onglet
            self.__tabFonction.append( ttk.Frame( frame ) )
            # On y ajoute les label et entry
            self.__editsFonction.append( self.createLblAndTxt( self.__tabFonction[i], ge ) )
            # On ajoute l'onglet au panel des fonctions
            subFrame.add( self.__tabFonction[i], text = ge.nom )
        subFrame.grid( column = 0, columnspan = 3 )
        return subFrame
        
    def createSolverPanel( self, frame ) :
        """
            Creer le notebook et les onglets pour la gestion du solver et du graphique
            @param frame le panel general ou les onglets doivent etre integres
        """
        subFrame = ttk.Notebook( frame )        
        # Onglet du solver
        tabSolver = ttk.Frame( subFrame )
        subFrame.add( tabSolver, text = self.__geSolver.nom )
            # On cree les radiobuttons
        self.__rbValueSolver = tk.StringVar( tabSolver, "1" ) 
        for (text, value) in self.__rbSolver.items(): 
            i = int( value )-1
            tk.Radiobutton( tabSolver, text = text, variable = self.__rbValueSolver, value = value,
                           command = self.handleSolverRB ).grid( row = 0, column = i, padx = 1, pady = 1 )
            # On cree les labels et les textes editables lies au solver
        lblSolver, entriesSolver = [ ], [ ]
        for i in range( len( self.__geSolver.lbls ) ) :
            lblSolver.append( tk.Label( tabSolver, text = self.__geSolver.lbls[i] ) )
            lblSolver[i].grid( row = i+1, column = 0, padx = 1, pady = 1 )        
        
            entriesSolver.append( tk.Entry( tabSolver ) )
            entriesSolver[i].insert( 0, self.__geSolver.edits[i] )
            entriesSolver[i].grid( row = i+1, column = 1, padx = 1, pady = 1 )
        self.__paramSolver = [ lblSolver, entriesSolver ]
            # On ajoute 1 bouton (pour lancer le solveur)
        self.__btnSolve = tk.Button( tabSolver, text = "Lancer", command = self.solve )
        self.__btnSolve.grid( row = 4, column = 0, padx = 1, pady = 1 )
        
        # Onglet du graphique
            # On cree un onglet
        tabGraph = ttk.Frame( subFrame )
        subFrame.add( tabGraph, text = self.__geGraph.nom )
            # On y ajoute les label et entry
        self.__editsGraph = self.createLblAndTxt( tabGraph, self.__geGraph )
            # On ajoute 2 boutons (pour dessiner et remettre a 0)
        self.__btnDraw = tk.Button( tabGraph, text = "Dessiner", command = self.draw )
        self.__btnDraw.grid(row = len(self.__editsGraph), column = 0, padx = 1, pady = 1 )
        tk.Button( tabGraph, text = "Reset", command = self.reset ).grid(row = len(self.__editsGraph), column = 1, padx = 1, pady = 1 )
        
        # On "pack" pour mettre en place sur l'interface
        subFrame.pack( )
        
    def createDrawPanel( self ) :
        frame = tk.Frame( self.master, relief = "groove" )
        self.__canvas = tk.Canvas( self.master, bg = "white", height = self.__sizeGraph[0], width = self.__sizeGraph[1] )
        self.__canvas.pack( )
        frame.pack( side = "right" )

    def createLblAndTxt( self, tab, guiElement ) :
        entries = [ ]
        # Pour chaque parametre de la fonction
        for i in range( len(guiElement.lbls) ) :
            # On cree un label dans une frame de type grid (pour avoir lbl et edit cote a cote)
            tk.Label( tab, text = guiElement.lbls[i] ).grid( row = i, column = 0, padx = 1, pady = 1 )
            # On cree un texte editable
            entries.append( tk.Entry( tab, width = 35 ) )
            entries[i].insert( 0, guiElement.edits[i] )
            entries[i].grid( row = i, column = 1, padx = 1, pady = 1 )  
        # Et on renvoie les textes editables (pour pouvoir recuperer les chaines plus tard)
        return entries
        
        
    # =============================================================================
    #     Callbacks / Gestion des evenements
    # =============================================================================
    def draw( self ) :
        """
           Appui sur le bouton "Dessiner" de l'onglet "Graphique"
           Efface le graphe precedent, retrace les axes et la fonction
           en fonction des valeurs xMin, xMax, yMin et yMax
        """
        # Supprime les dessins precedents
        self.__canvas.delete( "all" )
        # Limites des axes
        H = self.__sizeGraph[0]
        W = self.__sizeGraph[1]
        xMin = float( self.__editsGraph[0].get( ) )
        xMax = float( self.__editsGraph[1].get( ) )
        yMin = float( self.__editsGraph[2].get( ) )
        yMax = float( self.__editsGraph[3].get( ) )
        # Valeur en px de 0
        xOrigPx = round( -W * xMin / (xMax - xMin) )
        yOrigPx = round( H * yMax / (yMax - yMin) )
        # Conversion
            # x -> px: px = W (x - xMin) / (xMax - xMin)
            # y -> px: px = H (yMax - y) / (yMax - yMin)
        # /!\ Inversion des axes (0,0) est en haut a gauche
        # Dessin des axes
        self.__canvas.create_line( xOrigPx, 0, xOrigPx, H, fill = "black", width = 2 )   # Verticale
        self.__canvas.create_line( 0, yOrigPx, W, yOrigPx, fill = "black", width = 2 )   # Horizontale
        
        # Dessin de la fonction
        if self.__fcn :
            nbPts = round( W / 2 )
            dX = (xMax - xMin) / nbPts
            xP, yP = xMin, self.__fcn.getValeur( xMin )
            xPPx = round( W * (xP - xMin) / (xMax - xMin) )
            yPPx = round( H * (yMax - yP) / (yMax - yMin) )
            for x in range( nbPts ) :
                x = xP + dX
                y = self.__fcn.getValeur( x )
                xPx = round( W * (x - xMin) / (xMax - xMin) )
                yPx = round( H * (yMax - y) / (yMax - yMin) )
                self.__canvas.create_line( xPPx, yPPx, xPx, yPx, fill = "blue", width = 2 )
                xP, yP = x, y
                xPPx, yPPx = xPx, yPx
        
    def reset( self ) :
        """
            Appui sur le bouton "Reset" de l'onglet "Graphique"
            Remet les valeurs de xMin, xMax, yMin et yMax aux valeurs initiales
            puis retrace le graphique
        """
        for i, gEdit in enumerate( self.__editsGraph ) :
            gEdit.delete( 0, tk.END )
            gEdit.insert( 0, self.__geGraph.edits[i] )
        self.draw( )
            
    
    def handleSolverRB( self ) :
        """
            Gestion des radiobuttons du solveur
            En fonction du choix (Dichotomie / Newton ):
                renomme le label xMin / x0
                (des)active l'Entry xMax (inutile dans Newton)            
        """
        if self.__rbValueSolver.get( ) == "1" :
            self.__paramSolver[0][1].config( text = "xMin" )
            self.__paramSolver[0][2].config( state = "normal" )
            self.__paramSolver[1][2].config( state = "normal" )
        else :
            self.__paramSolver[0][1].config( text = "x0" )
            self.__paramSolver[0][2].config( state = "disabled" )
            self.__paramSolver[1][2].config( state = "disabled" )
            
            
            
    def ajouterFonction( self ) :
        # On recupere le choix de l'utilisateur et les zones de texte associees
        choix = self.__nbFonction.index( self.__nbFonction.select( ) )
        edits = self.__editsFonction[choix]
        # Selon le choix, on cree la fonction (conversion des textes en float)
        if choix == 0 :
            coef = [ float( c ) for c in edits[0].get( ).split( "," ) ]
            fcn = Polynome( coef )
        elif choix == 1 :
            ampl = float( edits[0].get( ) )
            freq = float( edits[1].get( ) )
            phase = float( edits[2].get( ) )
            fcn = Sinus( ampl, freq, phase )
        else :
            a = float( edits[0].get( ) )
            b = float( edits[1].get( ) )
            fcn = Exponentielle( a, b )
        # Si la fonction n'existe pas deja dans la liste
        if fcn not in self.__fcnList :
            # On ajoute la fonction a la liste de fonctions et on recree la somme de fonctions
            self.__fcnList.append( fcn )
            self.__fcn = SommeFonction( self.__fcnList )
            # On met a jour la liste deroulante
            txt = str( len( self.__fcnList ) ) + ": " + str( fcn )
            if len( self.__fcnList ) > 1 :
                self.__cboxFcn['values'] += (txt, )
            else :
                self.__cboxFcn['values'] = (txt, )
            # On active la combobox et les boutons car au moins un element
            self.__btnDel.config( state = "normal" )
            self.__btnPrint.config( state = "normal" )        
            self.__cboxFcn.config( state = "readonly" )
            self.__cboxFcn.current(0)
            # Et on affiche un petit message
            self.__txtLog.insert(tk.END, "Fonction ajoutee: {}\n".format(fcn) )
        else :
            self.__txtLog.insert(tk.END, "Erreur: Fonction deja presente!\n" )
            
    def supprimerFonction( self ) :
        # On recupere l'index de la fonction a supprimer
        idx, fcnText = self.__cboxFcn.get( ).split( ": " )
        idx = int( idx ) - 1
        # On supprime la fonction de la liste et recree la somme de fonctions
        del self.__fcnList[ idx ]
        self.__fcn = SommeFonction( self.__fcnList )
        # On met a jour la combobox
        values = [ str( i+1 ) + ": " + str( fcn ) for i, fcn in enumerate( self.__fcnList ) ]
        self.__cboxFcn.config( values = values )
        # On desactive les boutons et la combobox si plus aucune fonction
        if not self.__fcnList :
            self.__btnDel.config( state = "disabled" )
            self.__btnPrint.config( state = "disabled" )        
            self.__cboxFcn.config( state = "disabled" )
            
            self.__fcn = None
        else :
            self.__cboxFcn.current( 0 )
            
        self.__txtLog.insert(tk.END, "Fonction supprimee: {}\n".format( fcnText ) )
            
    def afficherFonction( self ) :
        self.__txtLog.insert(tk.END, "f(x) = {}\n".format( self.__fcn ) )
        
            
    def solve( self ) :
        """
            Cherche le 0 d'une fonction :
                Cree une fonction "Somme"
                Recupere le choix de Solveur
                Calcule et affiche le resultat
        """
        if self.__fcn :
            eps = float( self.__paramSolver[1][0].get( ) )
            s = Solveur( self.__fcn, eps )
            if self.__rbValueSolver.get( ) == "1" :
                xMin = float( self.__paramSolver[1][1].get( ) )
                xMax = float( self.__paramSolver[1][2].get( ) )
                self.__txtLog.insert(tk.END, "Solveur ({}): Dichotomie entre {} et {}\n".format( eps, xMin, xMax ) )
                res = s.dichotomie( xMin, xMax )
            else :
                x0 = float( self.__paramSolver[1][1].get( ) )
                self.__txtLog.insert(tk.END, "Solveur ({}): Newton depuis {}\n".format( eps, x0 ) )
                res = s.newton( x0 )
            self.__txtLog.insert(tk.END, "La solution a f(x) = 0 est x = {}\n".format( res ) )
        else :
            self.__txtLog.insert(tk.END, "Erreur: vous devez d'abord definir une fonction\n" )
        

root = tk.Tk()
app = FonctionSolveur( root )
app.mainloop()