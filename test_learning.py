import utils_learning
import strategy
import strategy_learning

team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

team1.add( "Cavani", strategy_learning.ShootingLearningStrat( ) )  
team2.add( "Aurier", strategy_learning.StaticStrategy( ) )

simu = strategy.Simulation( team1, team2 )

obs = utils_learning.Observer( simu )

strategy.show_simu( simu )

simu.start( )
