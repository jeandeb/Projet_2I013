# -*- coding: utf-8 -*-<

from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
import tools
import basic_strategy



GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 # Acceleration maximale de la balle

## Strategie aleatoire


class CenterStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "Random" )

    def compute_strategy( self, state, id_team, id_player ):
  
        return SoccerAction( Vector2D.create_random( -0.5, 0.5 ), Vector2D.create_random( -0.5, 0.5 ) )
        
class FonceurStrategy( Strategy ):
    def __init__( self ):

        Strategy.__init__( self, "Fonceur" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.fonceur( state )

class StrikerStrategy( Strategy ):
    def __init__( self ):
        Strategy.__init__( self, "Striker" )
            
    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.striker(state )
    

class DefenceStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Defence" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.defence(state )
        
class DefenceOffStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "DefenceOff" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action(prop )
        
        return basic_strategy.defence_off(state )

    
class SoloStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Solo" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.solo(state )
    
    
class SolosupStrategy(Strategy):
    def __init__( self ):
        Strategy.__init__( self, "Solo" )

    def compute_strategy( self, state, id_team, id_player ):
        
        prop =  tools.properties(state,id_team,id_player )
        state = tools.basic_action( prop )
        
        return basic_strategy.solosup(state)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




