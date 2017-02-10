# -*- coding: utf-8 -*-<
from soccersimulator.mdpsoccer import SoccerState, PlayerState, Ball
import strategy_learning
import strategy
from soccersimulator.utils import JSONable, Vector2D
from soccersimulator import settings

team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

#team1.add( "Cavani", strategy_learning.StaticStrategy( ) )
team1.add( "Cavani", strategy_learning.ShootingLearningStrat( ) )  
team2.add( "Aurier", strategy_learning.StaticStrategy( ) )

#def writeInfo(  ) : 
#On peux faire iterer les x et y en redefinissant a chaque fois
#la méthode
#peut eter qu'il faut inclure une fonction dans ncis et ainsi ne pas avoir
#redefinir ncis mais la fonction elle même, ou ses paramètres
#Definition des points ou vont apparaitre les joueurs
x = 135
y = 45

#inutile
def position_x( x ):
	return x
def position_y( y ): 
	return y

#creer un etat initial pour apprendre les tirs
@classmethod
def new_create_initial_state( cls, nb_players_1=0, nb_players_2=0 ) : 

	state = cls()
	quarters = [i * settings.GAME_HEIGHT / 4. for i in range(1, 4)]
	rows = [settings.GAME_WIDTH * 0.1, settings.GAME_WIDTH * 0.35, settings.GAME_WIDTH * (1 - 0.35), settings.GAME_WIDTH * (1 - 0.1)]
    		
	state.states[(1, 0)] = PlayerState(position=Vector2D( x, y ) )
	state.states[(2, 0)] = PlayerState(position=Vector2D(50, 50))
	state.ball = Ball.from_position( x, y )

	return state

SoccerState.create_initial_state = new_create_initial_state


#def writeInfo(  )

#Creation d'une partie
simu = strategy.Simulation( team1, team2 )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )