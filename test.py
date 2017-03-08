# -*- coding: utf-8 -*-<

import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

#team1.add( "Cavani", strategy.FonceurStrategy( ) ) 
team1.add( "Aurier", strategy.DefenceStrategy( ) )
team1.add( "Sarko", strategy.StrikerStrategy( ) )
team2.add( "Sarko", strategy.FonceurStrategy( ) )
team2.add( "JLM", strategy.DefenceStrategy( ) )    
#team2.add( "Hollande", strategy.StrikerStrategy( ) )
#team2.add( "Fillon", strategy.DefenceStrategy( ) )
#team2.add( "IEUoeio", strategy.StrikerStrategy( ) )
#Creation d'une partie
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )

