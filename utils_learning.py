from soccersimulator.utils import Vector2D
from soccersimulator.mdpsoccer import Ball
from soccersimulator import settings
import strategy

class Observer( object ):
    MAX_STEP = 20
    
    def __init__(self, simu):
        self.simu = simu
        self.simu.listeners += self
        
    def begin_match( self, team1, team2, state ):
        self.simu.state.states[(1,0)].position=Vector2D(130,45)
        self.simu.state.states[(2,0)].position=Vector2D(0,0)
        self.simu.state.ball = Ball( Vector2D(130,45) ) 
        self.last, self.cpt, self.cpt_tot = 0, 0, 0
        
    def begin_round( self, team1, team2, state ):
        self.simu.state.states[(1,0)].position=Vector2D(130,45)
        self.simu.state.states[(2,0)].position=Vector2D(0,0)
        self.simu.state.ball = Ball( Vector2D(130,45) ) 
        
    def update_round(self,team1,team2,state):
        if state.step > self.last + self.MAX_STEP : 
            self.simu.end_round()
            
    def end_round(self,team1,team2,state):
        if state.goal > 0 :
            self.cpt += 1
        self.cpt_tot += 1
        if self.cpt_tot > 1000 : 
            self.simu.end_match()
    
    
class Config_discrete( object ):
    
    def __init__( self ) :
        self.tab_config = 
        
    
        
        
