
import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

#team1.add( "Mahrez", strategy.StrikerStrategy( ) ) 
team1.add( "Aurier", strategy.StrikerStrategy( ) )
team2.add( "Toulalan", strategy.DefenceOffStrategy( ) )
#team2.add( "Henry", strategy.StrikerStrategy( ) )    

#Creation d'une partie
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )

