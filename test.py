# -*- coding: utf-8 -*-<

import strategy
import apprentissage_arbres
from arbres_utils import build_apprentissage,affiche_arbre,DTreeStrategy,apprend_arbre,genere_dot
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
dic = {"Fonceur":strategy.FonceurStrategy(),"DefPlacement":strategy.DefPlacement(),"Static":strategy.StaticStrategy()}
treeStrat1 = DTreeStrategy(dt,dic,my_get_features)
team2.add("Benzema",treeStrat1)


#Creation d'une partie
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )

