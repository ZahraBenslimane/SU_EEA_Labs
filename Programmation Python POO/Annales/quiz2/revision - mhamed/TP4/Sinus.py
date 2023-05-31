from math import pi, sin, cos
from Fonction import Fonction

class Sinus(Fonction) :

	def __init__( self, ampl, freq, phi ) :
		self.ampl = ampl	# Amplitude
		self.freq = freq	# Frequence
		self.phi = phi		# Phase a l'origine

	# Les properties
	@property
	def ampl( self ) :
		return self.__ampl
	@ampl.setter
	def ampl( self, ampl ) :
		self.__ampl = ampl
		
	@property
	def freq( self ) :
		return self.__freq
	@freq.setter
	def freq( self, freq ) :
		self.__freq = freq
		
	@property
	def phi( self ) :
		return self.__phi
	@phi.setter
	def phi( self, phi ) :
		self.__phi = phi
		
		
	def __str__( self, x = "x" ) :
		""" Conversion du sinus en une chaine de caracteres de la forme
		 	ampl * sin( 2 * pi * freq * x + phi )
			@param x (valeur par defaut: "x") une chaine de caractere correspondant a la variable x
		"""
		res = str(self.ampl) + " * sin( 2*pi*" + str(self.freq) + "*(" + x + ") + " + str(self.phi) + " ) "
		return res
	
	def __eq__( self, other ) :
		if( not isinstance( other, Sinus ) ) :
			return False
		if( self.ampl != other.ampl ) :
			return False
		if( self.freq == other.freq ) :
			return False
		if( self.phi == other.phi ) :
			return False
		return True
			
			
	def getValeur( self, x ) :
		"""	Calcul de la valeur de f(x)
			@param x point ou l'on souhaite calculer la valeur
			@return f(x)
		"""
		return ( self.ampl * sin( 2 *  pi * self.freq * x + self.phi ) )
	
	def getDerivee( self, x ) :
		"""	Calcul de la valeur de f'(x)
			@param x point ou l'on souhaite calculer la valeur
			@return f(x)
		"""
		return ( 2 * pi * self.freq * self.ampl * cos( 2 * pi * self.freq * x + self.phi ) )
