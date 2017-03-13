# -*- coding: utf-8 -*-<


import pickle
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
data_shoot = pickle.load( open( "tab_shoot.p", "rb" ) )


class properties( object ):
    def __init__( self,state,idteam,idplayer ):
        self.state = state
        self.key = ( idteam, idplayer )
        if self.key[0] == 1 : 
            self.owngoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.adgoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
            self.left = Vector2D( GAME_WIDTH/2, GAME_HEIGHT )
            self.right = Vector2D( GAME_WIDTH/2, 0 )
        else : 
            self.adgoal =  Vector2D( 0, GAME_HEIGHT/2 )
            self.owngoal =  Vector2D( GAME_WIDTH, GAME_HEIGHT/2. )
            self.left = Vector2D( GAME_WIDTH/2, 0 )
            self.right = Vector2D( GAME_WIDTH/2, GAME_HEIGHT )
        self.my_position =  self.state.player_state( self.key[0], self.key[1] ).position
        self.ball_position = self.state.ball.position
        self.ball_vitesse = self.state.ball.vitesse
        
    @property
    def pos_x( self ):
        return self.my_position.x

    @property
    def pos_y( self ):
        return self.my_position.y

    @property
    def vector_ball( self ) :
        return  self.ball_position - self.my_position
    @property
    def vector_ball_but(self):
        return self.ball_position -self.adgoal
    @property
    def dist_ball_but(self):
        return self.vector_ball_but.norm
    @property
    def dist_ball( self ) :
        return  self.vector_ball.norm
        
    def ball_area( self, dist ) : 
        return ( self.ball_position - self.owngoal ).norm < dist 
       
    @property   
    def vector_goal( self ):
        return self.adgoal - self.my_position

    @property 
    def dist_goal( self ): #Par rapport à ma posititon
        return self.vector_goal.norm

    @property
    def ball_side( self ):
        return not self.ball_area( GAME_WIDTH/2 - 2 )
 
    
    @property
    def can_shoot( self ) :
        if ( self.vector_ball ).norm >= PLAYER_RADIUS + BALL_RADIUS:
                return False
        return True

    @property
    def get_x_learn(self) : 
        x = self.pos_x
        if self.key[0] == 2 :
            x = GAME_WIDTH - x
        return x

    @property
    def get_y_learn(self) : 
        y = self.pos_y
        if self.key[0] == 2 :
            y = GAME_HEIGHT - y
        return y

    @property
    def can_shoot_learn( self ) :
        x = self.get_x_learn
        y = self.get_y_learn
        if not self.ball_side :
            return False
        if self.can_shoot and data_shoot.get_proba( x, y ) > 0.9  :
            return True
        return False
         
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
    
    def adv_players( self,where ):
        liste_ap = []
        for idt,idp in self.state.players : 
            if idt != self.key[0] :
                dist = ( self.state.player_state( idt, idp ).position - where ).norm
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

    def pos_dist_min_ad( self, where ) :

        dist_min =  self.dist_min( self.adv_players( where ) )
        return self.state.player_state( dist_min[0],  dist_min[1] ).position
    @property
    def norm_min_ad(self):
        return (self.my_position-self.pos_dist_min_ad(self.my_position)).norm
    
    @property
    def all_advplayers_behind( self ) : 

        cpt = 0;
        adv_players = self.adv_players(self.my_position)
        for idt, idp, dist in adv_players : 
            if ( ( self.my_position - self.adgoal ).norm < ( self.state.player_state( idt,  idp ).position - self.adgoal ).norm ) : 
                cpt += 1

        return cpt == len( adv_players ) 


    @property
    def anticipe_dir(self): #Anticipe la direction de la balle 
        return self.vector_ball + 15*self.ball_vitesse
        
    
    @property
    def near_play_ball( self ) :
        for idt,idp in self.state.players : 
                dist = ( self.state.player_state( idt, idp ).position - self.ball_position ).norm
                if dist < self.dist_ball:
                    return False
        return True
        

class basic_action( object ): 
    
    def __init__( self,properties ):
        self.prop = properties
    
    def passe( self,p ):
        
        dir_conduite = p - self.prop.my_position
        angle_con = dir_conduite.angle
        norm = dir_conduite.norm / 2

        return SoccerAction( Vector2D( ), Vector2D( angle = angle_con, norm = norm ) )
     
    def go( self,p ):
        dist_p = p - self.prop.my_position
        if dist_p.norm < 1:
            return SoccerAction( Vector2D( ),Vector2D( ) )
        return SoccerAction( p - self.prop.my_position,Vector2D( ) )
    
    @property    
    def go_ball( self ) : 
        return SoccerAction( self.prop.vector_ball,Vector2D( ) )
    
    @property
    def go_anticipe_ball( self ) : 
        return SoccerAction( self.prop.anticipe_dir, Vector2D() ) 
        
    def anticipe_ball(self,rayon):
        if self.prop.ball_vitesse.norm > rayon : 
            return self.go_anticipe_ball
        return self.go_ball
        
    #Calibrer le tir sur la distance par rapport au but
    @property
    def shoot_goal( self ):
        vector_shoot = self.prop.adgoal - self.prop.my_position
        return SoccerAction( Vector2D( ), vector_shoot.normalize()*2 )
      
    @property
    def shoot_learn( self ) :

        x = self.prop.get_y_learn
        y = self.prop.get_y_learn
    
        norm = data_shoot.get_norm( x, y )
        return SoccerAction( Vector2D( ), self.prop.vector_goal.normalize()*norm )


    @property
    def placement_def( self ):
        return self.go( ( self.prop.ball_position + self.prop.owngoal )/2 )
        
    @property #PAS BESOIN POUR LE MOMENT PEUT ETRE A SUPPRIMER
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
           return self.anticipe_ball(1)
        return SoccerAction( Vector2D( ), Vector2D( angle = angle_con, norm = norm ) )

    def grand_pont( self, angle, pos, angle_force, force ):

        if angle < 0 :
            return self.conduire( pos + Vector2D( 0, -angle_force ), force )
        return self.conduire( pos + Vector2D( 0, angle_force ), force )
        
    def marquage( self, p ):
        if self.prop.key[0] == 1 : 
            return self.go( p + Vector2D( -10, 0 ) )
        return self.go( p + Vector2D( 10, 0 ) )
        
    @property
    def marquage_att( self ):
        p = self.prop.pos_dist_min_ad( self.prop.owngoal )
        return self.marquage( p )
        
        

    #IL FAUT SIMPFLIFIER
    #Probleme on fait avec des angles ce qui nest pas symetrique
    @property
    def dribbler_but( self  ):

        #dist_adv = self.prop.dist_min
        pos_adv = self.prop.pos_dist_min_ad(self.prop.my_position)
        vec_adv = pos_adv - self.prop.my_position
        
        def_behind = ( ( self.prop.my_position - self.prop.adgoal ).norm < ( pos_adv - self.prop.adgoal ).norm )
        if vec_adv.norm < 20 and not def_behind : #valeur avant 30
            return self.grand_pont( vec_adv.angle, pos_adv, 5, 1.3 )

       # if vec_adv.norm < 30 and not def_behind:
        #    return self.grand_pont( vec_adv.angle, pos_adv, 30, 1 )            

        if self.prop.all_advplayers_behind :
            return self.conduire( self.prop.adgoal, 2.2 )

        return self.conduire( self.prop.adgoal, 1 )

    @property
    def solo_dribbler_but( self  ):

        #dist_adv = self.prop.dist_min
        pos_adv = self.prop.pos_dist_min_ad(self.prop.my_position)
        vec_adv = pos_adv - self.prop.my_position
        
        def_behind = ( ( self.prop.my_position - self.prop.adgoal ).norm <= ( pos_adv - self.prop.adgoal ).norm )

        if (vec_adv.norm < 30 or self.prop.ball_side) and not def_behind:
            return self.grand_pont( vec_adv.angle, pos_adv, -30, 1 )  

        if vec_adv.norm < 10 and not def_behind : #valeur avant 30
            return self.grand_pont( vec_adv.angle, pos_adv, -10, 2 )         

        if self.prop.all_advplayers_behind :
            return self.conduire( self.prop.adgoal, 2.2 )

        return self.conduire( self.prop.adgoal, 1 )
    
    #balek
    @property
    def roulette( self ):
        
        pos_adv = self.prop.pos_dist_min_ad(self.prop.my_position)
        vec_adv = pos_adv - self.prop.my_position
        if angle < 0 :
            return self.conduire( pos + Vector2D( 0, 8 ), 2.5 ) # j'ai remplacé 10 par 8 et -8
        return self.conduire( pos + Vector2D( 0, -8 ), 2.5 )

        vecteur_roulette = Vector2D( angle = vec_adv.angle + 1.5, norm = vec_adv.norm )
        return self.conduire( vecteur_roulette, 1.5 )
            
        
        

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        