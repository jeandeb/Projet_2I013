import numpy as np
from soccersimulator import settings
MAX_X = settings.GAME_WIDTH/2
MAX_Y = settings.GAME_HEIGHT

class discretedata( object ) : 
	

	def __init__( self ) :
		#stex, stepy, stepnorm"
		self.step_x = 3
		self.step_y = 3
		self.nb_x = MAX_X/self.step_x
		self.nb_y = MAX_Y/self.step_y
		self.tab_proba = np.zeros(( self.nb_x, self.nb_y ))
		self.tab_norm = np.zeros(( self.nb_x, self.nb_y ))

	def nb_x( self ) :
		return self.nb_x

	def nb_y( self ) :
		return self.nb_y

	def get_norm( self, x, y) :

		case_x = ( x - MAX_X )/self.nb_x
		case_y = y/self.nb_y

		return self.tab_norm[ case_x , case_y ]

	def set_norm( self, norm, x, y ) :

		case_x = ( x - MAX_X )/self.nb_x
		case_y = y/self.nb_y

		self.tab_norm[ case_x , case_y ] = norm
		

	def get_proba( self, x, y) :

		case_x = ( x - MAX_X )/ self.nb_x
		case_y = y/self.nb_y
		tmp = self.tab_proba[ case_x , case_y ]
		return tmp

	def set_proba( self, proba, x, y ) :
		case_x = ( x - MAX_X )/self.nb_x
		case_y = y/self.nb_y

		self.tab_proba[ case_x , case_y ] = proba

