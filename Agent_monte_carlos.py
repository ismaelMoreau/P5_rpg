import numpy as np
import p5
from settings import *
from collections import defaultdict
import time
import progressbar
from Particle_system import *
#TODO base class and ineheritance for different sections
class Agent_monte_carlos:
    def __init__(self,nb_row,nb_col,start_position_x,start_position_y,map,monsters,images) -> None:
        self.agent_position_x, self.agent_position_y = start_position_x,start_position_y
       
        self.agent_start_position_x, self.agent_start_position_y = start_position_x,start_position_y
        #self.grid = np.zeros(nb_row,nb_col)
        #self.q_values = np.zeros(nb_row,nb_col)
        self.ep_rewards = []
        self.map=map
        self.monsters = monsters
        self.is_visible=False
        self.images = images
        self.image_number = 12
        self.Q_table= np.zeros((TILECOL,TILEROW,4))
        
        self.epsilon=0.5
        self.thinking_mode = True
        self.path_to_a_monster = []
        self.step_max_by_episode = STARTINGNUMBEROFMOVESBYEPISODE
        self.lvl = 1
        self.is_on_monster = False
        self.sysParticle = ParticleSysteme(0,0)
        self.ai_thinking(NBEPISODES)


    def set_rewards(self,rewards_position):
        self.rewards_position = rewards_position
    
    def reset(self):
        return self.agent_start_position_x,self.agent_start_position_y
        
    def total_reset(self):
        self.agent_position_x,self.agent_position_y = self.agent_start_position_x,self.agent_start_position_y
        self.Q_table.fill(0)
        self.thinking_mode = True
       
        self.epsilon = 0.5
        self.image_number = 12
        self.ai_thinking(NBEPISODES)

    def draw_agent(self,screen_x,screen_y):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position_x*TILESIZE+10+offset_x,self.position_y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if (not(self.agent_position_x*TILESIZE<screen_x*TILESIZE+WIDTH) or not (self.agent_position_y*TILESIZE<screen_y*TILESIZE+HEIGHT+(-2*TILESIZE))
                or not(self.agent_position_x*TILESIZE>=screen_x*TILESIZE) or not(self.agent_position_y*TILESIZE>=screen_y*TILESIZE)):
                self.is_visible = False
                return
        p5.image(self.images[self.image_number].blend(self.images[self.image_number],"blend"),
            (self.agent_position_x - screen_x) * TILESIZE,(self.agent_position_y - screen_y)*TILESIZE,TILESIZE,TILESIZE)
        self.is_visible = True
   
    def step(self,action,x,y,monster_arr,map,lvl):
    
        if action == 0:#down
            y += 1
            #self.limit_coordinates()
            
        elif action == 1:#right
            x += 1
            #self.limit_coordinates()
            
        elif action == 2:#up
            y += -1
            #self.limit_coordinates()
           
        elif action == 3:#left
            x += -1
            #self.limit_coordinates()
            

        reward =-1
        done = False

        if map[x,y]==-1:
            r = np.random.sample()
            if r>(0.04*lvl):
                reward = -10
                done = True
                
                
        for monster in monster_arr :
            if (x,y) == monster:
                reward = 100
                done = True
        
        return x,y,reward,done
    
    def policy(self):
        action = np.random.randint(0,4)
        return action
        
    def generate_episode(self,x,y,Q,max_num_steps,monsters_pos,map,lvl):
        episode = []
        
        for t in range(max_num_steps):
            
            # Sélection d'une action en fonction de notre politique
            action = self.politique_egreedy(x,y,Q,self.epsilon)
            
            # envoie de l'action à l'environnement pour retour (s_, r, done)
            x_,y_,reward,done = self.step(action,x,y,monsters_pos,map,lvl)
            
            # stockage dans la liste du triplet (état, action, récompense)
            episode.append((x,y, action, reward))
            
            if done:
                break
                
            x,y = x_,y_

        return episode

    def politique_egreedy(self,x,y,Q,epsilon):
       
        r=np.random.uniform()
        
        if r<epsilon :# or action == self.last_action:
            if epsilon > 0.01: self.epsilon -= 0.01   
            #action = np.random.choice([i for i in range(0,4) if i != self.last_action])
            return np.random.choice(4)
        else:
            if epsilon > 0.01: self.epsilon -= 0.01
            return self.my_argmax(Q[x,y])

    def my_argmax(self,my_array):
        # notre argmax
        my_max=-10000.0
        my_list_of_max = []
        for i in range(0,my_array.shape[0]):
            if my_array[i] > my_max:
                my_max=my_array[i]
                my_list_of_max = [ i ]
            else:
                if my_array[i] == my_max:
                    my_list_of_max.append(i)
        return(np.random.choice(my_list_of_max))
        
    def ai_thinking(self,num_episodes):
        
        lvl = self.lvl
        Q = self.Q_table
        total_return = defaultdict(float)
        N = defaultdict(float)
        start_x,start_y = self.agent_position_x,self.agent_position_y
        monster_tupple_position = [(monster.map_position.x,monster.map_position.y) for monster in self.monsters]
        map = self.map
        gamma=0.8
        step_max = self.step_max_by_episode
        for i in progressbar.progressbar(range(num_episodes)):
            self.epsilon = 0.5
            # on génére un épisode
            episode = self.generate_episode(start_x,start_y,Q,step_max,monster_tupple_position,map,lvl)
            
            # on stocker les pairs s,a de l'épisode
            #all_state_action_pairs = [(s, a) for (s,a,r) in episodes]
            R= 0
            # on stocke les récompense
            rewards = [r for (x,y,a,r) in episode]

            # Pour chaque t de l'épisode 
            for t, (x,y, action, reward) in enumerate(episode):

                # First visit : on ne prend en compte que le premier passage s,a
                # if not (state, action) in all_state_action_pairs[0:t]:
                    
                    # Calcul de G avec y = 1
                    for num  in range(len(rewards)-1,t,-1):
                        R += rewards[num]*pow(gamma,num-t)

                    # Cumul G
                    total_return[(x,y,action)] +=  R
                    
                    # Comptage du nombre de passage
                    N[(x,y, action)] += 1

                    # Calcul de Q value (s,a) par la moyenne des G cumulés sur N
                    Q[x,y,action] = total_return[(x,y, action)] / N[(x,y, action)]
        #for val in N.values():
            # if len(episode) >100:
            #     print(len(episode))
        self.Q_table = Q
        self.thinking_mode = False


    def real_step(self,x,y,screen_vector):
        action = self.politique_egreedy(x,y,self.Q_table,epsilon=0.0)
        self.is_on_monster = False
        # pos = [self.agent_position_x,self.agent_position_y]
        # self.path_to_a_monster.append(pos)
        reset = False
        if action == 0:#down
            self.agent_position_y += 1
            
            self.image_number= np.random.randint(3)
        elif action == 1:#right
            self.agent_position_x += 1
            
            self.image_number= np.random.randint(3,6)
        elif action == 2:#up
            self.agent_position_y += -1
            
            self.image_number= np.random.randint(6,9)
        elif action == 3:#left
            self.agent_position_x += -1
            
            self.image_number= np.random.randint(9,12)
        
        if self.map[self.agent_position_x,self.agent_position_y]==-1:
            r = np.random.sample()
            if r>0.10*self.lvl:
                # self.path_to_a_monster.clear()
                reset = True
                self.map[self.agent_position_x,self.agent_position_y]=292
        for i,monster in enumerate(self.monsters):
            if self.agent_position_x == monster.map_position.x and self.agent_position_y == monster.map_position.y:
                self.monsters.pop(i)
                self.agent_start_position_x = self.agent_position_x
                self.agent_start_position_y = self.agent_position_y
                self.lvl += 1
                self.sysParticle.set_position((self.agent_position_x-screen_vector.x)*TILESIZE+(TILESIZE/2),(self.agent_position_y-screen_vector.y)*TILESIZE+(TILESIZE/2))
                self.sysParticle.add_particle(15)
                # for position in self.path_to_a_monster:
                #     self.Q_table[position[0],position[1],action]=sum(self.Q_table[position[0],position[1]])/4
                # self.path_to_a_monster.clear()
                self.is_on_monster = True
                reset = True
        if reset:
            self.total_reset()

    def run_particle_system(self):
        self.sysParticle.run()

        
    def empty_particles(self):
        self.sysParticle.particles.clear()