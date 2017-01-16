# -*- coding: utf-8 -*-
from soccer_base import *
from soccerobj import SoccerBall
import numpy as np
import time


###############################################################################
# SoccerAction
###############################################################################

class SoccerAction(object):
    def __init__(self,acceleration=Vector2D(),shoot=Vector2D()):
        self.acceleration=acceleration
        self.shoot=shoot
        
    def copy(self):
        return SoccerAction(self.acceleration,self.shoot)

        
###############################################################################
# SoccerState
###############################################################################
   
class SoccerState:
    def __init__(self,team1,team2,ball):
        self.team1=team1
        self.team2=team2
        self._winning_team=0
        self.ball=ball
        self._width=GAME_WIDTH
        self._height=GAME_HEIGHT
    def copy(self):
        res=SoccerState(self.team1.copy(),self.team2.copy(),self.ball.copy())        
        res._winning_team=self._winning_team        
        return res
    @property
    def winning_team(self):
        return self._winning_team
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def diagonal(self):
        return np.sqrt(self.width**2+self.height**2)
    
    def get_team(self,teamid):
        if teamid==1:
            return self.team1
        if teamid==2:
            return self.team2
        raise SoccerStateException("get_team : team demandé != 1 ou 2 : %s" % i)
        
    def get_player(self,num_team,player):
       return self.get_team(num_team).get_player(player)

    def get_goal_center(self,teamid):
        if (teamid==1):
            return Vector2D(0,self.height/2.)
        if (teamid==2):
            return Vector2D(self.width,self.height/2.)
        raise SoccerStateException("get_goal_center : team demandé != 1 ou 2 : %s" % i)
            
    def is_y_inside_goal(self,y):
        return np.abs(y-(self.height/2))<GAME_GOAL_HEIGHT/2

  
    """ implementation """
    
    def apply_action(self,player,action):
        if not action:
            return
        player.dec_num_before_shoot()
        action_shoot=action.shoot.copy()
        action_acceleration=action.acceleration.copy()
        if (player.position.distance(self.ball.position)<(PLAYER_RADIUS+BALL_RADIUS)):
            if (player.get_num_before_shoot()>0):
                action_shoot=Vector2D()
            else:
                player.init_num_before_shoot()
            if action_shoot.norm>maxPlayerShoot:
                action_shoot.product(1.0/action_shoot.norm * maxPlayerShoot)
            if action_shoot.norm>0:
                player_speed=Vector2D.create_polar(player.angle,player.speed)
                dot_p=action_shoot.dot(player_speed)/(action_shoot.norm*player_speed.norm)
                if player_speed.norm==0:
                    fake_speed=Vector2D.create_polar(player.angle,1)
                    dot_p=action_shoot.dot(fake_speed)/(action_shoot.norm*fake_speed.norm)
                dot_p+=2
                dot_p/=3.
                if (dot_p<0.5):
                    dot_p=0.5
                action_shoot.product(dot_p)
                action_shoot+=player_speed
                norm=action_shoot.norm
                angle=np.arctan2(action_shoot.y,action_shoot.x)
                angle+=(np.random.rand()*2.-1)*shootRandomAngle/180.*np.pi
                action_shoot=Vector2D.create_polar(angle,norm)
                self.sum_of_shoots+=action_shoot
                
        norm = action_acceleration.norm
        if norm>maxPlayerAcceleration:
            action_acceleration.product(1./norm*maxPlayerAcceleration)
        frotte=Vector2D.create_polar(player.angle,-player.speed)
        frotte.product(playerBrackConstant)
        resultante=frotte
        resultante+=action_acceleration        
        new_speed=Vector2D.create_polar(player.angle,player.speed)
        new_speed+=resultante
        new_player_speed=new_speed.norm
        if (new_player_speed>0):
            new_player_angle=np.arctan2(new_speed.y,new_speed.x)
            if new_player_speed>maxPlayerSpeed:
                new_player_speed=maxPlayerSpeed
                
            new_player_position=player.position.copy()
            new_player_position+=new_speed
            
            if new_player_position.x<0:
                new_player_position.x=0
                new_player_speed=0
            if new_player_position.y<0:
                new_player_position.y=0
                new_player_speed=0
            if new_player_position.x>self.width:
                new_player_position.x=self.width
                new_player_speed=0
            if new_player_position.y>self.height:
                new_player_position.y=self.height
                new_player_speed=0
            player.angle=new_player_angle
            player.speed=new_player_speed
            player.position=new_player_position
        
    def apply_actions(self,team1_actions,team2_actions):
        self.sum_of_shoots=Vector2D()
        for player,action in team1_actions.iteritems():
            self.apply_action(self.get_player(1,player),action)
        for player,action in team2_actions.iteritems():
            self.apply_action(self.get_player(2,player),action)

        frotte_ball_square=self.ball.speed.copy()
        coeff_frottement_square=ballBrakeSquare*(self.ball.speed.norm**2)
        frotte_ball_square.product(-coeff_frottement_square)
        frotte_ball_constant=self.ball.speed.copy()
        coeff_frottement_constant=ballBrakeConstant
        frotte_ball_constant.product(-coeff_frottement_constant)
        
        new_ball_speed=self.ball.speed
        no=self.sum_of_shoots.norm
        if no!=0:
            if (no>maxBallAcceleration):
                self.sum_of_shoots.product(1./no*maxBallAcceleration)
            new_ball_speed=self.sum_of_shoots.copy()
        new_ball_speed+=frotte_ball_square
        new_ball_speed+=frotte_ball_constant
        
        self.ball.speed=new_ball_speed
        new_ball_position=self.ball.position
        new_ball_position+=new_ball_speed
        self.ball.position=new_ball_position
        
        pos=self.ball.position
        speed=self.ball.speed
        if pos.x<0:
            if self.is_y_inside_goal(pos.y):
                self._winning_team=2
            else:
                self.ball.position=Vector2D(-pos.x,pos.y)
                self.ball.speed=Vector2D(-speed.x,speed.y)
        if pos.y<0:
            self.ball.position=Vector2D(pos.x,-pos.y)
            self.ball.speed=Vector2D(speed.x,-speed.y)
        if pos.x>self.width:
            if self.is_y_inside_goal(pos.y):
                self._winning_team=1
            else:
                self.ball.position=Vector2D(self.width-(pos.x-self.width),pos.y)
                self.ball.speed=Vector2D(-speed.x,speed.y)
        if pos.y>self.height:
            self.ball.position=Vector2D(pos.x,self.height-(pos.y-self.height))
            self.ball.speed=Vector2D(speed.x,-speed.y)
    def __str__(self):
        return str(self.ball)+"\n"+ str(self.team1)+"\n"+str(self.team2)

###############################################################################
# SoccerBattle
###############################################################################
   
class SoccerBattle(object):
    def __init__(self,team1,team2):
        if team1.num_players != team2.num_players:
            raise BattleException("Les equipes n'ont pas le meme nombre de joeurs")
        self.team1=team1
        self.team2=team2
        self.score=Score()
        self.listeners=SoccerEvents()
    @property
    def num_players(self):
        return self.team1.num_players
    def start_by_thread(self,battles_count,max_steps,father):
        self._father=father
        self.run_multiple_battles(battles_count,max_steps)
    def run_multiple_battles(self,battles_count=1,max_steps=MAX_GAME_STEPS):
        if not max_steps:
            max_steps=MAX_GAME_STEPS
        self.listeners.begin_battles(battles_count)                  
        for i in range(battles_count):            
            self.run(max_steps)
        self.listeners.end_battles()
        self._father=None                
    def start_battle(self,state):
        self.team1.start_battle(state)
        self.team2.start_battle(state) 
        self.listeners.start_battle(state)
    def finish_battle(self,state):
        if state.winning_team==0:
            self.team1.finish_battle(0)
            self.team2.finish_battle(0)
        if state.wining_team==1:
            self.team1.finish_battle(1)
            self.team2.finish_battle(-1)
        if state.winning_team==2:
            self.team1.finish_battle(-1)
            self.team2.finish_battle(1)
        self.listeners.finish_battle(state.winning_team)
            
    def run(self,max_steps):
            state=self.create_initial_state()
            result=-1
            self.start_battle(state.copy())
            for i in range(max_steps):
                st=state.copy()
                state.apply_actions(st.team1.compute_strategies(st,1),st.team2.compute_strategies(st,2))
                self.listeners.update_battle(state,i)                
                while  sum(self.listeners.is_ready())!=len(self.listeners):
                    time.sleep(0.0001)
                if state.winning_team>0:
                    break
                if self._father and self._father.stop_thread:
                    break                    
            self.score.add_result(state.winning_team)
            return state.winning_team

    def create_initial_state(self):
        state=SoccerState(self.team1.copy(),self.team2.copy(),SoccerBall())
        quarters=[i*state.height/4 for i in range(1,4)]
        rows=[state.width*0.1,state.width*0.35,state.width*(1-0.35),state.width*(1-0.1)]
        if self.num_players!=1 and self.num_players!=2 and self.num_players !=4:
            raise IncorrectTeamException("create_initial_state : Nombre de joueurs incorrects %d" % self.num_players)
        if self.num_players==1:
            state.team1[0].set_position(rows[0],quarters[1],0)
            state.team2[0].set_position(rows[3],quarters[1],np.pi)
        if self.num_players==2:
            state.team1[0].set_position(rows[0],quarters[0],0)
            state.team1[1].set_position(rows[0],quarters[2],0)
            state.team2[0].set_position(rows[3],quarters[0],np.pi)
            state.team2[1].set_position(rows[3],quarters[2],np.pi)
        if self.num_players==4:
            state.team1[0].set_position(rows[0],quarters[0],0)
            state.team1[1].set_position(rows[0],quarters[2],0)
            state.team1[2].set_position(rows[1],quarters[0],0)
            state.team1[3].set_position(rows[1],quarters[2],0)
            state.team2[0].set_position(rows[3],quarters[0],np.pi)
            state.team2[1].set_position(rows[3],quarters[2],np.pi)
            state.team2[2].set_position(rows[2],quarters[0],np.pi)
            state.team2[3].set_position(rows[2],quarters[2],np.pi)
        state.ball.position.x=state.width/2
        state.ball.position.y=state.height/2
        return state
         


class Events(object):
   def __init__(self):
       for e in self.__events__:
           self.__getattr__(e)
   def __getattr__(self, name):
      if hasattr(self.__class__, '__events__'):
         assert name in self.__class__.__events__, \
                "Event '%s' is not declared" % name
      self.__dict__[name] = ev = _EventSlot(name)
      return ev
   def __str__(self): return 'Events :' + str(list(self))
   __repr__ = __str__
   def __len__(self): 
       if len(self.__dict__)!=0: 
           return len(self.__dict__.values()[0])
       return 0
   def __iter__(self):
      def gen(dictitems=self.__dict__.items()):
         for attr, val in dictitems:
            if isinstance(val, _EventSlot):
               yield val
      return gen()

class _EventSlot(object):
   def __init__(self, name):
      self.targets = []
      self.__name__ = name
   def __repr__(self):
      return self.__name__
   def __call__(self, *a, **kw):
      return [ f(*a, **kw)  for f in self.targets]
   def __iadd__(self, f):
      self.targets.append(f)
      return self
   def __isub__(self, f):
      while f in self.targets: self.targets.remove(f)
      return self
   def __len__(self):
       return len(self.targets)

class SoccerEvents(Events):
    __events__=('begin_battles','start_battle','update_battle','finish_battle','end_battles','is_ready')
    def __iadd__(self,f):
        for e in self:
            try:
                e+=getattr(f,str(e))
            except:
                print "no %s supported by this interface" %e
        return self
    def __isub__(self, f):
        for e in self:
            while getattr(f,e) in e.targets: e.targets.remove(getattr(f,e))
        return self
            
            
