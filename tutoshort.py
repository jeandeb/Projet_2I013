from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
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

## Strategie aleatoire


def NearestPlayer( state, id_team, id_player ) :
    dist_min = GAME_WIDTH + GAME_HEIGHT
    id_min = id_player
    for i in state.players : 
        if i.id_team == id_team :
            diff = VectorLength( i.position -  state.player_state( id_team, id_player ).position )
            if( diff < dist_min and i != id_player ) :
                dist_min = diff
                id_min = i
    return i


class CenterStrategy( Strategy ) : 
    def __init__( self ):

        Strategy.__init__( self, "Random" )

    def compute_strategy( self, state, id_team, id_player ):

        return SoccerAction( Vector2D.create_random( -0.5, 0.5 ), Vector2D.create_random( -0.5, 0.5 ) )

class RandomStrategy( Strategy ):

    def __init__( self ):

        Strategy.__init__( self, "Random" )

    def compute_strategy( self, state, id_team, id_player ):

        return SoccerAction( Vector2D.create_random( -0.5, 0.5 ), Vector2D.create_random( -0.5, 0.5 ) )
        
class FonceurStrategy( Strategy ):
    def __init__( self ):

        Strategy.__init__( self, "Fonceur" )

    def compute_strategy( self, state, id_team, id_player ):
        
        state = tools.MyState(state,id_team,id_player )
        
        if not state.can_shoot( ) : 
           return state.go_ball( )
           
        return state.shoot_goal( )



class DefenceStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Defence" )

    def compute_strategy( self, state, id_team, id_player ):
        
        state = tools.MyState(state,id_team,id_player )
        
        
        if state.is_goal( ) :
             if not state.can_shoot( ) : 
                 return state.go_ball( )
             return state.shoot_goal( )
            
            
        if not state.ball_move( ):
            return state.placement( )
            
        if not state.can_shoot( ) : 
           return state.go_ball( )
           
        return state.shoot_goal( )
        

## Creation d'une equipe
team1 = SoccerTeam( name = "team1" ,login = "etu1" )
team2 = SoccerTeam( name = "team2", login = "etu2" )

##team1.add( "Johny", FonceurStrategy( ) ) 
team1.add( "Pierre", DefenceStrategy( ) )
##team2.add( "Yannis", DefenceStrategy( ) )
team2.add( "Larti", FonceurStrategy( ) )    

#Creation d'une partie
simu = Simulation( team1, team2 )
#Jouer et afficher la partie
show_simu( simu )
#Jouer sans afficher
simu.start( )
