# -*- coding: utf-8 -*-<
from soccersimulator.mdpsoccer import SoccerState, PlayerState, Ball, Simulation, SoccerAction
import strategy_learning
import strategy
from soccersimulator.utils import Vector2D
from soccersimulator import settings

team1 = strategy.SoccerTeam( name = "team1" ,login = "etu1" )
team2 = strategy.SoccerTeam( name = "team2", login = "etu2" )

#team1.add( "Cavani", strategy_learning.StaticStrategy( ) )
team1.add( "Cavani", strategy_learning.StaticStrategy( ) )  
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
#creer un etat initial pour apprendre les tirs

def new_get_initial_state_shoot(state):
    
    initial_state.states[(1, 0)] = PlayerState(position=Vector2D( x, y ) )
    initial_state.states[(2, 0)] = PlayerState(position=Vector2D(50, 50))
    initial_state.ball = Ball( Vector2D(x, y) )

    return initial_state
    
    
#Simulation.get_initial_state = new_get_initial_state_shoot
#state = SoccerState.create_initial_state(1,1)
#state.player(1,0).position = Vector2D( x, y )
#state.player(1,1).position = Vector2D( 0, 0 )
#state.ball.position = Vector2D( x, y )
#state.apply_actions({(1,0) : SoccerAction( Vector2D(1,1), Vector2D()), (1,1) : SoccerAction( Vector2D(), Vector2D()) })

#Creation d'une partie
simu = strategy.Simulation( team1, team2, state )
#Jouer et afficher la partie
strategy.show_simu( simu )
#Jouer sans afficher
simu.start( )