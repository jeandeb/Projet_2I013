

def fonceur( basic_action ):
    
    if not basic_action.prop.can_shoot : 
           return basic_action.go_anticipe_ball
           
    return basic_action.shoot_goal
    
def passeur( basic_action ):
    prop = basic_action.prop
    if not prop.can_shoot : 
           return basic_action.go_anticipe_ball
      
    nearplayer = prop.pos_dist_min
    return basic_action.passe( nearplayer )
    
def defence_off( basic_action ):
    
    prop = basic_action.prop
    if prop.dist_goal < 30:
        return fonceur( basic_action )
    
    if prop.dist_ball < 3 :
        return basic_action.solo_dribbler_but
    if prop.ball_area( 50 ) or prop.near_play_ball:
        return basic_action.go_anticipe_ball     
    

        
    return basic_action.placement_def
        

         
   # if not prop.can_shoot : 
    #    return basic_action.go_anticipe_ball
   
   # return basic_action.go_anticipe_ball       
   # return basic_action.shoot_goal

#NE FONCTIONNE PAS
def solo( basic_action ):
    prop = basic_action.prop

    if not prop.ball_move : 
        return fonceur( basic_action )
        
    if prop.can_shoot_learn  :
        return basic_action.shoot_learn

    if not prop.ball_area( 20 ) :
        return basic_action.solo_dribbler_but 

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

    if prop.near_play_ball :#or prop.ball_area( 20 ):
        return passeur( basic_action ) 

    if prop.ball_side:
        return basic_action.placement_def

    if not prop.ball_move : 
       return basic_action.anticipe_ball(1)   

    if not prop.ball_side: #or not prop.ball_move:
        return basic_action.marquage_att
        
        
def striker( basic_action ):
    
    prop = basic_action.prop
    
    if prop.can_shoot_learn  :
        return basic_action.shoot_learn

    if prop.ball_side or prop.dist_ball < 20  :

        return basic_action.dribbler_but
        
    return basic_action.placement_att_sup