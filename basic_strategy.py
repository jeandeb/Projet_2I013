

def fonceur( basic_action ):
    prop = basic_action.prop
    if not prop.ball_move : 
        return fonceur_base( basic_action )

    if not basic_action.prop.can_shoot :
        return basic_action.anticipe_ball( 2 )
           
    return basic_action.shoot_learn

def fonceur_base( basic_action ):
    prop = basic_action.prop
    if not basic_action.prop.can_shoot and basic_action.prop.can_shoot.ball_move : 
           return basic_action.go_ball
    if  basic_action.prop.can_shoot : 
        return basic_action.shoot_goal_max
    return basic_action.go_ball
    
def passeur( basic_action ):

    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.anticipe_ball( 2 )
      
    nearplayer = prop.pos_dist_min( prop.my_position )
    return basic_action.passe( nearplayer )

def passeurtest( basic_action ):

    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.anticipe_ball( 2 )
      
    
    return basic_action.shoot_goal_max

def passeur_retrait( basic_action ):
    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.anticipe_ball( 2 )
      
    nearplayer = prop.pos_dist_min( prop.owngoal )
    return basic_action.passe( nearplayer )

def passeur_attaque( basic_action ):
    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.anticipe_ball( 2 )
      
    nearplayer = prop.pos_dist_min( prop.adgoal )
    return basic_action.passe( nearplayer )
    
def defence_off( basic_action ):
    
    prop = basic_action.prop
    if prop.dist_goal < 30:
        return fonceur( basic_action )
    
    if prop.dist_ball < 3 :
        return basic_action.solo_dribbler_but
    if prop.ball_area( 50 ) or prop.near_play_ball:
        return basic_action.anticipe_ball( 2 )     
    

        
    return basic_action.placement_def
        

         
   # if not prop.can_shoot : 
    #    return basic_action.go_anticipe_ball
   
   # return basic_action.go_anticipe_ball       
   # return basic_action.shoot_goal

#NE FONCTIONNE PAS
def solo( basic_action ):
    prop = basic_action.prop

    if not prop.ball_move and prop.ball_center : 
        return fonceur_base( basic_action )

        
    if prop.can_shoot_learn  :
        return basic_action.shoot_learn

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but

    return basic_action.anticipe_ball( 2 )
        
def solosup(basic_action):
    prop=basic_action.prop
   
    
    if prop.dist_goal < 30 :

        return fonceur( basic_action )

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but
        
    return basic_action.go_ball    
        
        
def conduite_but( basic_action ):

    prop = basic_action.prop

    return basic_action.conduire( prop.adgoal, 1 )
    
    
#AMELIORER LE DFENSEURS POUR QU'IL FASSE DES PASSES ET NON DES DEGAGEMENTS
def defence( basic_action ):

    prop = basic_action.prop

    if prop.ball_area( 45 ) and prop.near_play_ball:
        return passeur( basic_action ) 
        
    if prop.ball_side or not prop.ball_move:
        return basic_action.placement_def
         
    if prop.can_shoot : 
        return passeur_attaque( basic_action ) 

    return basic_action.anticipe_ball( 1 )

def goal( basic_action ):

    prop = basic_action.prop
    if prop.can_shoot : 
        #return passeur( basic_action )
        return basic_action.shoot_goal_max
    if prop.ball_area( 30 ) and prop.near_play_ball:
        return basic_action.anticipe_ball( 1 )

    if not prop.ball_area( 20 ) : 
        return basic_action.placement_goal
                 

    return basic_action.anticipe_ball( 1 )

def defence_4( basic_action ):
    
    prop = basic_action.prop

    if prop.near_play_ball :#or prop.ball_area( 20 ):
        return passeur( basic_action ) 

    if prop.ball_side:
        return basic_action.placement_def

    if not prop.ball_move : 
       return basic_action.anticipe_ball(1.5)   

    if not prop.ball_side: #or not prop.ball_move:
        return basic_action.marquage_att

def defencetest( basic_action ):

    prop = basic_action.prop

    if prop.ball_area( 45 ) and prop.near_play_ball:
        return passeurtest( basic_action ) 
        
    if prop.ball_side or not prop.ball_move:
        return basic_action.placement_def
         
    if prop.can_shoot : 
        return basic_action.shoot_goal_max 

    return basic_action.anticipe_ball( 1 )        
        
        
def striker( basic_action ):
    
    prop = basic_action.prop
    
    if not prop.ball_move and prop.ball_center : 
        return fonceur_base( basic_action )

    if prop.can_shoot_learn  :
        return basic_action.shoot_learn

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but
        
    return basic_action.placement_att_sup
    
def striker_4( basic_action ):
    
    prop = basic_action.prop

    if prop.team_ball : 
        basic_action.campeur

    if prop.can_shoot_learn  :
        return basic_action.shoot_learn

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but
        
    return basic_action.placement_att_sup_4

def center( basic_action ):
    
    prop = basic_action.prop

    if prop.can_shoot_learn :
        return basic_action.shoot_learn

    if not prop.ball_move : 
        return defence( basic_action )

    if prop.near_play_ball or prop.ball_area( 40 ) : 
        return passeur_attaque( basic_action )


    return basic_action.placement_center

    
    
def placementdef(basic_action):
    return basic_action.placement_def