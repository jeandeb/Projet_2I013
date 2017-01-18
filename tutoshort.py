from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
import math

GAME_WIDTH = 150 # Longueur du terrain
GAME_HEIGHT = 90 # Largeur du terrain
GAME_GOAL_HEIGHT = 10 # Largeur des buts
PLAYER_RADIUS = 1. # Rayon d un joueur
BALL_RADIUS = 0.65 # Rayon de la balle
MAX_GAME_STEPS = 2000 # duree du jeu par defaut
maxPlayerSpeed = 1. # Vitesse maximale d un joueur
maxPlayerAcceleration = 0.2 # Acceleration maximale
maxBallAcceleration = 5 # Acceleration maximale de la balle

but2 = Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
but1 = Vector2D( 0, GAME_HEIGHT/2 )
## Strategie aleatoire
def VectorLength( vector ) : 
    return ( vector.x ** 2 + vector.y ** 2 ) ** ( 0.5 )

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
        
class AttackStrategy( Strategy ):
    def __init__( self ):

        Strategy.__init__( self, "Attack" )

    def compute_strategy( self, state, id_team, id_player ):

        tirbut2 = but2 - state.player_state( id_team, id_player ).position
        tirbut1 = but1 - state.player_state( id_team, id_player ).position

        if id_team == 1:
            return SoccerAction( state.ball.position - state.player_state( id_team, id_player ).position, tirbut2 )
        else:
            return SoccerAction( state.ball.position - state.player_state( id_team, id_player ).position, tirbut1 )
            
class DefenceStrategy( Strategy ):

    def __init__( self ):
        Strategy.__init__( self, "Defence" )

    def compute_strategy( self, state, id_team, id_player ):

        p_position = state.player_state( id_team, id_player ).position
        tirbut2 = but2 - state.player_state( id_team, id_player ).position
        tirbut1 = but1 - state.player_state( id_team, id_player ).position

        if state.ball.vitesse.x > 0 or state.ball.vitesse.y > 0 :

            if id_team == 1:
                 return SoccerAction( state.ball.position - p_position, tirbut2 )

            else:
                return SoccerAction( state.ball.position - p_position, tirbut1 ) 
            

        if p_position.x >=  GAME_WIDTH/2 :
            return SoccerAction( Vector2D( GAME_WIDTH/2 - p_position.x, GAME_HEIGHT/2 - p_position.y ), Vector2D( 0, 0 ) )


        if id_team == 1:
            positiondef = ( state.ball.position + but1)/2 - p_position
            
            return SoccerAction( positiondef, tirbut2 )

        else:
            positiondef = ( state.ball.position + but2 )/2 - p_position
            return SoccerAction( positiondef, tirbut1 )
        

## Creation d'une equipe
team1 = SoccerTeam( name = "team1" ,login = "etu1" )
team2 = SoccerTeam( name = "team2", login = "etu2" )

team1.add( "Johny", DefenceStrategy() ) 
team1.add( "Pierre", AttackStrategy() )
#team2.add( "Yannis", AttackStrategy() )
#team2.add( "Larti", DefenceStrategy() )    

#Creation d'une partie
simu = Simulation( team1, team2 )
#Jouer et afficher la partie
show_simu( simu )
#Jouer sans afficher
simu.start()
