import strategy

## Creation d'une equipe
team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

team1.add( "Johny", strategy.StrikerStrategy( ) ) 
#team1.add( "Pierre", strategy.DefenceStrategy( ) )
#team2.add( "Yannis", strategy.DefenceStrategy( ) )
team2.add( "Larti", strategy.FonceurStrategy( ) )    
