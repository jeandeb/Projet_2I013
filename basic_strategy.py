import tools


class basic_strategy(object):
    
    def __init__(self,basic_action):
        self.ba=tools.basic_action
    
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
            return basic_action.go_ball
               
        return basic_action.shoot_goal
    
    def solo( basic_action ):
    
        prop = basic_action.prop
        if prop.ball_side:
            return defence_off( basic_action )
    
            if not prop.can_shoot : 
                return basic_action.go_ball 
            return basic_action.dribbler_but
    
        return basic_action.dribbler_but
    
    def conduite_but( basic_action ):
    
        prop = basic_action.prop
    
        return basic_action.conduire( prop.adgoal, 1 )
        
        
    #AMELIORER LE DFENSEURS POUR QU'IL FASSE DES PASSES ET NON DES DEGAGEMENTS
    def defence( basic_action ):
        
        prop = basic_action.prop
        if prop.ball_area( 45 ) :
            return passeur( basic_action ) 
            
        if prop.ball_side or not prop.ball_move:
            return basic_action.placement_def
             
        if not prop.can_shoot : 
            return basic_action.go_ball
               
        return basic_action.shoot_goal
            
    def striker( basic_action ):
        
        prop = basic_action.prop
        
        if prop.dist_goal < 30 :
    
            return fonceur( basic_action )
    
        if prop.ball_side or prop.dist_ball < 20  :
    
            return basic_action.dribbler_but
            
        return basic_action.placement_att_sup