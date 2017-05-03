from soccersimulator import settings, utils
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import basic_strategy
import strategy_learning
import searchclass
import dataclass
import pickle
import numpy as np
import logging

data = dataclass.discretedata()

expe = searchclass.ShootSearch( data )

expe.start( False )

print data.tab_proba
print data.tab_norm

pickle.dump( data, open( "tableau_learning/tab_shoot3.p", "wb" ) )
