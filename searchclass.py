from soccersimulator import settings
from soccersimulator import SoccerTeam, Simulation, Strategy, show_simu, Vector2D, SoccerAction
import tools
import basic_strategy
import strategy_learning
import dataclass

import numpy as np
import logging

logger = logging.getLogger("simuExpe")

class ShootSearch(object):
    """ nombre d'iterations maximales jusqu'a l'arret d'un round
        discr_step  : pas de discretisation du parametre
        nb_essais : nombre d'essais par parametre
    """
    MAX_STEP = 40

    def __init__(self):
        self.data = dataclass.discretedata()

        self.strat = ShootingLearningStrat()

        team1 = SoccerTeam("Testeur")
        team1.add("Expe",self.strat)

        team2 = SoccerTeam("Immobile")
        team2.add("Static",Strategy())

        self.simu = Simulation( team1,team2,max_steps=1000000)

        self.simu.listeners+=self

        self.nb_tirs_case = 10

        self.step = data.nb_x() * data.nb_y()

        self.step_cpt = 0;


    def start(self,visu=True):
        """ demarre la visualisation avec ou sans affichage"""
        if visu :
            show_simu(self.simu)
        else:
            self.simu.start()

    def begin_match(self,team1,team2,state):
        """ initialise le debut d'une simulation
            res : dictionnaire des Resultats
            last : step du dernier round pour calculer le round de fin avec MAX_STEP
            but : nombre de but pour ce parametre
            cpt : nombre d'essais pour ce parametre
        """
        self.last = 0
        self.but = 0
        self.cpt = 0
        

    def begin_round(self,team1,team2,state):
        """ engagement : position random du joueur et de la balle """
        position = Vector2D()
        self.simu.state.states[(1,0)].position = position.copy()
        self.simu.state.states[(1,0)].vitesse = Vector2D()
        self.simu.state.ball.position = position.copy()
        self.strat.norm = self.params[self.idx]
        self.last = self.simu.step

    def update_round(self,team1,team2,state):
        """ si pas maximal atteint, fin du tour"""

        if state.step > self.last + self.MAX_STEP:
            self.simu.end_round()

    def end_round(self,team1,team2,state):


        """ si tous les tirs ont été fait a toutes les cases, enmatch"""
        if self.cpt >= self.step * self.nb_tirs_case : 
            self.simu.end_match()







