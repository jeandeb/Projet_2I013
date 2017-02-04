from soccersimulator.strategies  import Strategy
from soccersimulator.mdpsoccer import SoccerTeam, Simulation, SoccerAction
from soccersimulator.gui import SimuGUI,show_state,show_simu
from soccersimulator.utils import Vector2D
import tools
import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

team1.add( "Johny", strategy.DefenceOffStrategy( ) ) 
#team1.add( "Pierre", strategy.DefenceStrategy( ) )
team2.add( "Yannis", strategy.DefenceStrategy( ) )
team2.add( "Larti", strategy.StrikerStrategy( ) )    
