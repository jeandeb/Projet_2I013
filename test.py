# -*- coding: utf-8 -*-<

import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "AS FORBACH" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "MFC", login = "etu2" )

team1.add( "Cavani", strategy.FonceurStrategy( ) ) 
#team1.add( "Aurier", strategy.DefenceStrategy( ) )
#team1.add( "Sarko", strategy.StrikerStrategy( ) )
#team2.add( "Sarko", strategy.SoloStrategy( ) )
#team2.add( "JLM", strategy.CenterStrategy( ) )    
#team2.add( "Hollande", strategy.StrikerStrategy( ) )
#team2.add( "Fillon", strategy.DefenceOffStrategy( ) )
#team2.add( "IEUoeio", strategy.StrikerStrategy( ) )
team2.add( "Aurier", strategy.SoloStrategy( ) )
#Creation d'une partie
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )

