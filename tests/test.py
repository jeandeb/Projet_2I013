


import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "AS FORBACH" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "MFC", login = "etu2" )

#team2.add( "Cavani", strategy.FonceurStrategy( ) ) 
#team1.add( "Aurier", strategy.DefenceStrategy( ) )
#team1.add( "Sarko", strategy.StrikerStrategy( ) )
#team1.add( "Sarko", strategy.SoloStrategy( ) )
#team2.add( "JLM", strategy.CenterStrategy( ) )    
#team2.add( "Hollande", strategy.StrikerStrategy( ) )
#team2.add( "Fillon", strategy.DefenceOffStrategy( ) )
#team2.add( "IEUoeio", strategy.StrikerStrategy( ) )
team1.add( "Aurier", strategy.SoloStrategy( ) )
#Creation d'une partie
#test4
#team1.add( "Striker", strategy.StrikerStrategy( ) )
#team1.add( "Center", strategy.CenterStrategy( ) )
#team1.add( "Defence", strategy.DefenceStrategy( ) )
#team1.add( "Defence", strategy.DefenceStrategy( ) )

team2.add( "Fonceur", strategy.FonceurStrategy( ) ) 
#team2.add( "Striker", strategy.Striker4Strategy( ) )
#team2.add( "Defence", strategy.DefenceStrategy( ) )
#team2.add( "Defence", strategy.CenterStrategy( ) )
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )