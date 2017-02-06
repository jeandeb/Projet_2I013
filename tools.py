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

class properties( object ):
    def __init__( self,state,idteam,idplayer ):
        self.state=state
        self.key=( idteam,idplayer )
        if self.key[0] == 1 : 
            self.owngoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.adgoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
        else : 
            self.adgoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.owngoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
        self.my_position =  self.state.player_state( self.key[0], self.key[1] ).position
        self.ball_position = self.state.ball.position
        self.ball_vitesse = self.state.ball.vitesse
        
    @property
    def vector_ball( self ) :
        return  self.ball_position - self.my_position
        
    @property
    def dist_ball( self ) :
        return  self.vector_ball.norm
        
    def ball_area( self, dist ) : 
        return ( self.ball_position - self.owngoal ).norm < dist 
       
    @property   
    def vector_goal( self ):
        return self.adgoal - self.my_position

    @property 
    def dist_goal( self ):
        return self.vector_goal.norm

    @property
    def ball_side( self ):
        return not self.ball_area( GAME_WIDTH/2 )
 
    
    @property
    def can_shoot( self ) :
        if ( self.vector_ball ).norm >= PLAYER_RADIUS + BALL_RADIUS:
                return False
        return True
         
    @property
    def ball_move( self ):
        return self.state.ball.vitesse.x > 0 or self.state.ball.vitesse.y > 0  
    
    #MAUVAIS CODAGE, IL Y A UN COPIER COLLER, ESSAYER DE FUSIONNER LES DEUX FONCTIONS, ET QU'ELLES MARCHENT MEME LORQU'IL N'Y A QU'UN SEUL JOUEUR
    @property
    def team_players( self ):
        liste_tp = []
        for idt,idp in self.state.players : 
            if idt == self.key[0] and idp != self.key[1] :
                dist = (  self.state.player_state( idt, idp ).position - self.my_position ).norm
                liste_tp.append( [idt,idp, dist] )
        return liste_tp
    
    @property
    def adv_players( self ):
        liste_ap = []
        for idt,idp in self.state.players : 
            if idt != self.key[0] :
                dist = ( self.state.player_state( idt, idp ).position - self.my_position ).norm
                liste_ap.append( [idt,idp, dist] )
        return liste_ap     
    
    
    def dist_min( self, liste ):

        mini = GAME_WIDTH + GAME_HEIGHT
        idteam = 0
        idmin = 0

        for i in liste:

            if i[2] < mini :    
                mini = i[2]
                idmin = i[1]
                idteam = i[0]

        return [ idteam, idmin ]
    
    @property
    def pos_dist_min( self ) :

        dist_min =  self.dist_min( self.team_players )
        return self.state.player_state( dist_min[0],  dist_min[1] ).position

    @property
    def pos_dist_min_ad( self ) :

        dist_min =  self.dist_min( self.adv_players )
        return self.state.player_state( dist_min[0],  dist_min[1] ).position
    
    @property
    def all_advplayers_behind( self ) : 

        cpt = 0;

        for idt, idp, dist in self.adv_players : 
            if ( ( self.my_position - self.adgoal ).norm < ( self.state.player_state( idt,  idp ).position - self.adgoal ).norm ) : 
                cpt += 1

        return cpt == len( self.adv_players ) 


    @property
    def anticipe_dir(self):
        return self.vector_ball + 10*self.ball_vitesse
        

    
   
    
    

class basic_action( object ): 
    
    def __init__( self,properties ):
        self.prop = properties
    
    def passe( self,p ):
        
        dir_conduite = p - self.prop.my_position
        angle_con = dir_conduite.angle
        norm = dir_conduite.norm / 2

        return SoccerAction( Vector2D( ), Vector2D( angle = angle_con, norm = norm ) )
     
    def go( self,p ):
        return SoccerAction( p-self.prop.my_position,Vector2D( ) )
    
    @property    
    def go_ball( self ) : 
        return SoccerAction( self.prop.vector_ball,Vector2D( ) )
    
    @property
    def go_anticipe_ball( self ) : 
        return SoccerAction( self.prop.anticipe_dir, Vector2D() ) 
        
    #Calibrer le tir sur la distance par rapport au but
    @property
    def shoot_goal( self ):
        
        return SoccerAction( Vector2D( ),self.prop.adgoal - self.prop.my_position )
        
    @property
    def placement_def( self ):
        return self.go( ( self.prop.ball_position + self.prop.owngoal )/2 )
        
    @property #PAS BESOIN POUR LE MOMENT
    def placement_att( self ):
        if self.prop.ball_side :
            return self.go( Vector2D( GAME_WIDTH + 3, GAME_HEIGHT ) )
            
    @property
    def placement_att_sup( self ):
        nearplayer = self.prop.pos_dist_min 
        if self.prop.key[0] == 1 : 
            return self.go( nearplayer + Vector2D( 50, 0 ) )
        return self.go( nearplayer + Vector2D( -50, 0 ) )
        
    def conduire( self, point_direction, norm ):

        dir_conduite = point_direction - self.prop.my_position
        angle_con = dir_conduite.angle

        if not self.prop.can_shoot : 
           return self.go_ball

        return SoccerAction( Vector2D( ), Vector2D( angle = angle_con, norm = norm ) )

    def grand_pont( self, angle, pos ):

        if angle < 0 :
            return self.conduire( pos + Vector2D( 0, 10 ), 2.5 )
        return self.conduire( pos + Vector2D( 0, -10 ), 2.5 )
        


    #IL FAUT SIMPFLIFIER
    @property
    def dribbler_but( self  ):

        #dist_adv = self.prop.dist_min
        pos_adv = self.prop.pos_dist_min_ad
        vec_adv = pos_adv - self.prop.my_position

        def_behind = ( ( self.prop.my_position - self.prop.adgoal ).norm < ( pos_adv - self.prop.adgoal ).norm )
        if vec_adv.norm < 30 and not def_behind : 

            return self.grand_pont( vec_adv.angle, pos_adv )

        if self.prop.all_advplayers_behind :
            return self.conduire( self.prop.adgoal, 2 )

        return self.conduire( self.prop.adgoal, 1 )
        
        
def fonceur( basic_action ):
    
    if not basic_action.prop.can_shoot : 
           return basic_action.go_ball
           
    return basic_action.shoot_goal
    
def passeur( basic_action ):
    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.go_ball
      
    nearplayer = prop.pos_dist_min
    return basic_action.passe( nearplayer )
    
def defence_off( basic_action ):
    
    prop = basic_action.prop
    if prop.ball_area( 30 ) :
        return fonceur( basic_action )
                      
    if not prop.ball_move:
        return basic_action.placement_def

         
    if not prop.can_shoot : 
        return basic_action.go_anticipe_ball
           
    return basic_action.shoot_goal

#NE FONCTIONNE PAS
def solo( basic_action ):
    prop = basic_action.prop
    if prop.ball_area( 30 ) :
        return fonceur( basic_action )
    if not prop.ball_move:
        return basic_action.placement_def

    if not prop.can_shoot : 
        return basic_action.go_ball

    return basic_action.dribbler_but

def conduite_but( basic_action ):

    prop = basic_action.prop

    return basic_action.conduire( prop.adgoal, 1 )
    
    
#AMELIORER LE DFENSEURS POUR QU'IL FASSE DES PASSES ET NON DES DEGAGEMENTS
def defence( basic_action ):
    
    prop = basic_action.prop
    if prop.ball_area( 50 ) :
        return passeur( basic_action ) 
        
    if prop.ball_side or not prop.ball_move:
        return basic_action.placement_def
         
    if not prop.can_shoot : 
        return basic_action.go_anticipe_ball
           
    return basic_action.shoot_goal
        
def striker( basic_action ):
    
    prop = basic_action.prop
    
    if prop.dist_goal < 30 :

        return fonceur( basic_action )

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but
        
    return basic_action.placement_att_sup
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        