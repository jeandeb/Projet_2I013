# -*- coding: utf-8 -*-<


from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
import strategy


def get_team( i ):
    MFC = SoccerTeam( name = "MFC"  )
    if i==1:
        MFC.add( "Johny", strategy.DefenceOffStrategy( ) ) 
    if i == 2 :
        MFC.add( "Yannis", strategy.DefenceStrategy( ) )
        MFC.add( "Cavani", strategy.StrikerStrategy( ) )
    return MFC
    
    
