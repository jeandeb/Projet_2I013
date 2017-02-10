# -*- coding: utf-8 -*-<

from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D, dump
import tools



GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 # Acceleration maximale de la balle



class ShootingLearningStrat( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "shooting_learning" )

	def end_round( self, team1, team2, state ) :
		self.listeners.end_round(self.team1, self.team2, self.state)
		#prop =  tools.properties(state,id_team,id_player )
			#f.write( "" + prop.my_position.x + " " +  prop.my_position.y )
		f = open( "learning_shoot.txt" ,"w")
		f.write( "lol" )
		f.close()
		pass

    def compute_strategy( self, state, id_team, id_player ):
    	prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )

        return state.shoot_goal





class StaticStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "shooting_learning" )

    def compute_strategy( self, state, id_team, id_player ):

        return SoccerAction( Vector2D(), Vector2D() )