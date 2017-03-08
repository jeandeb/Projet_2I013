from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import basic_strategy
import strategy_learning
import searchclass


import numpy as np
import logging


expe = searchclass.ShootSearch()


expe.start( False )

for i in range( expe.data.nb_x ) :
    for j in range( expe.data.nb_y ) :
        x = i * expe.data.step_x
        y = j * expe.data.step_y
        print( "x =  "+ str(x) + " y = " + str(y) + "norm = " + str(expe.data.get_norm( x, y )) + " proba = " + str(expe.data.get_proba( x, y ))  )