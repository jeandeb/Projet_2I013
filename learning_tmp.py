from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import basic_strategy
import strategy_learning
import searchclass


import numpy as np
import logging


expe = searchclass.ShootSearch()
expe.start( )