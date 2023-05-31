from math import exp
from Fonction import Fonction

class Exponentielle(Fonction) :
	
	def __init__( self, a, b ) :
		""" On a f(x) = a*exp(b*x) """
		self.a = a
		self.b = b

	# Les properties
	@property
	def a( self ) :
		return self.__a
	@a.setter
	def a( self, a ) :
		self.__a = a
		
	@property
	def b( self ) :
		return self.__b
	@b.setter
	def b( self, b ) :
		self.__b = b
		
		
	def __str__( self, x = "x" ) :
		""" Conversion de l'eponentielle en une chaine de caracteres de la forme
				a*exp(b*x)
			@param x (valeur par defaut: "x") une chaine de caractere correspondant a la variable x
		"""
		res = str(self.a) + " * exp( " + str(self.b) + " *(" + x + ") ) ";	
		return res
		
	def __eq__( self, other ) :
		if( not isinstance( other, Exponentielle ) ) :
			return False
		if( self.a != other.a ) :
			return False
		if( self.b != other.b ) :
			return False
		return True


	def getValeur( self, x ) :
		"""	Calcul de la valeur de f(x)
			@param x point ou l'on souhaite calculer la valeur
			@return f(x)
		"""
		return self.a * exp( self.b * x )
	
	def getDerivee( self, x ) :
		"""	Calcul de la valeur de f'(x)
			@param x point ou l'on souhaite calculer la valeur
			@return f(x)
		"""
		return self.b * self.getValeur( x )
		
