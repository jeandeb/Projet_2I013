from soccersimulator import settings, utils
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import basic_strategy
import strategy_learning
import searchclass
import dataclass

import numpy as np
import logging

data = dataclass.discretedata()
#utils.dump_jsonz( data, "tab_shoot" )
expe = searchclass.ShootSearch( data )
expe.start( False )
print data.tab_proba
print data.tab_norm

utils.dump_jsonz( data, "tab_shoot.jz" )
#for i in range( expe.data.nb_x ) :
 #   for j in range( expe.data.nb_y ) :
  #      x = i * expe.data.step_x
   #     y = j * expe.data.step_y
    #    print( "x =  "+ str(x) + " y = " + str(y) + "norm = " + str(expe.data.get_norm( x, y )) + " proba = " + str(expe.data.get_proba( x, y ))  )