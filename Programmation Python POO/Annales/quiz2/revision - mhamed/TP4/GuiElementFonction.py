class GuiElementFonction :
    def __init__( self, nom, lbls, edits ) :
        self.nom = nom
        self.lbls = lbls
        self.edits = edits
        
    
def createGuiElementFonction( ) :
    res = [ ]
    res.append( GuiElementFonction ( "Polynome", [ "Coefficients" ], [ "1.2, -0.1, -1.3, 0.1, 0.1" ] ) )
    res.append( GuiElementFonction ( "Sinus", [ "Amplitude", "Frequence", "Phase" ], [ "1", "0.2", "0" ] ) )
    res.append( GuiElementFonction ( "Exponentielle", [ "a", "b" ], [ "-1", "0.2" ] ) )
    return res 

def createGuiElementGraph( ) :
    res = GuiElementFonction ( "Graphique", [ "xMin", "xMax", "yMin", "yMax" ], [ "-5", "5", "-5", "5" ] )
    return res

def createGuiElementSolver( ) :
    res = GuiElementFonction ( "Solver", [ "Precision", "xMin", "xMax" ], [ "0.001", "-3", "3" ] )
    return res