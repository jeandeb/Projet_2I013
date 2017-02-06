from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
import strategy

def get_team( i ):
    MFC = SoccerTeam( name = "MFC"  )
    if i==1:
        MFC.add( "Johny", strategy.DefenceOffStrategy( ) ) 
    if i == 2 :
        MFC.add( "KiïLl€èèRdùuü75", strategy.DefenceStrategy( ) )
        MFC.add( "moi", strategy.StrikerStrategy( ) )
    return MFC
    
    
