#from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
#from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D

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
class MyState(object):

    def __init__(self,state,idteam,idplayer):
        self.state=state
        self.key=(idteam,idplayer)
        if self.key[0] == 1 : 
            self.owngoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.adgoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
        else : 
            self.adgoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.owngoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
        self.my_position =  self.state.player_state( self.key[0], self.key[1] ).position
        self.ball_position = self.state.ball.position
    
    def go(self,p):
        return SoccerAction(p-self.my_position,Vector2D())
    
    def shoot(self,p):
        return SoccerAction(Vector2D(),p-self.my_position)
        
    def vector_ball(self) :
        return  self.ball_position - self.my_position
    
    def go_ball(self) : 
        return SoccerAction(self.vector_ball(),Vector2D())
        
    def is_goal(self) : 
        if (self.ball_position - self.owngoal).norm < 30 :
            return True
        return False
        
    def can_shoot(self) :
        if ( self.vector_ball() ).norm >= PLAYER_RADIUS + BALL_RADIUS:
                return False
        return True
    
    def shoot_goal(self):
        return SoccerAction(Vector2D(),self.adgoal-self.my_position)
        
        
    def ball_move(self):
        return self.state.ball.vitesse.x > 0 or self.state.ball.vitesse.y > 0         
        
    def placement(self):
        return self.go((self.ball_position + self.owngoal)/2 )
    
        
        
        
        
        
        