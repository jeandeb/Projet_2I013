import numpy as np


class discretedata( object ) : 
	MAX_X = GAME_WIDTH/2
	MAX_Y = GAME_HEIGHT

	def __init__( self ) :
		#stex, stepy, stepnorm"
		self.step_x = 3
		self.step_y = 3
		self.tab_proba = np.zero(( self.nb_x, self.nb_y ))
		self.tab_norm = np.zero(( self.nb_x, self.nb_y ))

	def nb_x( self ) :
		return MAX_X/step_x

	def nb_y( self ) :
		return MAX_Y/step_y

	def get_norm( self, x, y) :

		case_x = x/nb_x()
		case_y = y/nb_x()

		return tab_norm.np( case_x, case_y )

	def set_norm( self, norm, x, y ) :

		case_x = x/nb_x()
		case_y = y/nb_x()

		tab_norm.np( case_x , case_y ) = norm

	def get_proba( self, x, y) :

		case_x = x/nb_x()
		case_y = y/nb_x()

		return tab_proba.np( case_x, case_y )

	def set_proba( self, proba, x, y ) :

		case_x = x/nb_x()
		case_y = y/nb_x()

		tab_proba.np( case_x , case_y ) = proba

