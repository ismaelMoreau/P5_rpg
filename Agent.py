import numpy as np
import p5
from settings import *
import time

#TODO base class and ineheritance for different sections
class Agent:
    def __init__(self,nb_row,nb_col,start_position_x,start_position_y,map,monsters,images) -> None:
        self.agent_position_x, self.agent_position_y = start_position_x,start_position_y
        self.agent_futur_position_x, self.agent_futur_position_y = start_position_x,start_position_y
        self.agent_start_position_x, self.agent_start_position_y = start_position_x,start_position_y
        #self.grid = np.zeros(nb_row,nb_col)
        #self.q_values = np.zeros(nb_row,nb_col)
        self.ep_rewards = []
        self.map=map
        self.monsters = monsters
        self.is_visible=False
        self.images = images
        self.image_number = 12
        self.Qlearning_table= np.zeros((TILECOL,TILEROW,4))
        
        self.epsilon=0.5
        self.thinking_mode = True
        self.last_action = 0
        self.monster_tupple_position = [(monster.map_position.x,monster.map_position.y) for monster in monsters]
       

    def set_rewards(self,rewards_position):
        self.rewards_position = rewards_position
    
    def reset(self):
        self.agent_position_x,self.agent_position_y = self.agent_start_position_x,self.agent_start_position_y
        self.agent_futur_position_x,self.agent_futur_position_y = self.agent_start_position_x,self.agent_start_position_y
        
    def total_reset(self):
        self.agent_position_x,self.agent_position_y = self.agent_start_position_x,self.agent_start_position_y
        self.agent_futur_position_x,self.agent_futur_position_y = self.agent_start_position_x,self.agent_start_position_y
        #self.Qlearning_table.fill(0)
        self.thinking_mode = True
        self.epsilon = 0.5
        self.monster_tupple_position = [(monster.map_position.x,monster.map_position.y) for monster in self.monsters]

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
   
    def step(self,action,x,y,monster_arr,map):
    
        if action == 0:#down
            y += -1
            #self.limit_coordinates()
            
        elif action == 1:#right
            x += 1
            #self.limit_coordinates()
            
        elif action == 2:#up
            y += 1
            #self.limit_coordinates()
           
        elif action == 3:#left
            x += -1
            #self.limit_coordinates()
            

        reward =-1
        done = False

        if map[x,y]==-1:
            # r = np.random.sample()
            # if r<0.25:
                reward = 10
                done = True
                
                
        for monster in monster_arr :
            if (x,y) == monster:
                reward = 100
                done = True
         
        # elif self.agent_position == self.rewards_position:
        #     reward = 0
        #     done = True
        # else:
        #     reward = -1 
        #     done = False
        
        return x,y,reward,done
    
    def policy(self):
        action = np.random.randint(0,4)
        return action

    def limit_coordinates(self):
        self.agent_futur_position_x = min(self.agent_futur_position_x, 60)
        self.agent_futur_position_x = max(self.agent_futur_position_x, 30)
        self.agent_futur_position_y = min(self.agent_futur_position_y, 60)
        self.agent_futur_position_y = max(self.agent_futur_position_y, 30)
        
    def episode(self):
        x,y = self.agent_position_x, self.agent_position_y 
        monsters = self.monster_tupple_position
        map = self.map
        Q = self.Qlearning_table
        gamma = 0.8
        alpha = 0.5
        #print(self.Qlearning_table)
        N=0
        done=False
        A =self.politique_egreedy(self.epsilon)
        while not done:
            N+=1
            x_,y_,R,done = self.step(A,x,y,monsters,map)
                
            A_=self.politique_egreedy(self.epsilon)
            
            Q[x,y,A] += alpha*(R+pow(gamma,N)*Q[x_,y_,A_] -Q[x,y,A])
            
            # # pour debug affichage
            # if verbose :
            #print(f"From S={x,y},A={A} to S_={x_,y_},A_={A_} R={R}")
            #     if done:
            #         print("----------------------------------------------------")
            x,y= x_,y_
            A = A_
            # reward , done = self.move(self.policy())
            # if not done:
            #     pass
            # else:
            #     self.reset()
        self.Qlearning_table = Q
        self.last_action = A

    def politique_egreedy(self,epsilon):
       
        r=np.random.uniform()
        action = self.my_argmax(self.Qlearning_table[self.agent_position_x,self.agent_position_y])
        if r<epsilon or self.backward(action)== self.last_action:# or action == self.last_action:
            
            #action = np.random.choice([i for i in range(0,4) if i != self.last_action])
            return np.random.choice(4)
        if epsilon > 0.01: self.epsilon -= 0.01
        self.last_action = action
        return action


            # autre solution
            # listQ=[]
            #for a in range(env.action_space.n):
            #    listQ.append(Q[s,a])
            # return(np.argmax(listQ)) 

    def backward(self,action):
        if action == 0:
            return 2
        elif action == 1:
            return 3
        elif action == 2:
            return 0
        elif action == 3:
            return 1


    def my_argmax(self,my_array):
        # notre argmax
        my_max=-1000000.0
        my_list_of_max = []
        for i in range(0,my_array.shape[0]):
            if my_array[i] > my_max:
                my_max=my_array[i]
                my_list_of_max = [ i ]
            else:
                if my_array[i] == my_max:
                    my_list_of_max.append(i)
        return(np.random.choice(my_list_of_max))
        
    def real_step(self):
        action = self.politique_egreedy(epsilon=0.0)
        self.Qlearning_table[self.agent_position_x,self.agent_position_y,action] = 0
        if action == 0:#down
            self.agent_position_y += -1
            self.limit_coordinates()
            self.image_number= np.random.randint(3)
        elif action == 1:#right
            self.agent_position_x += 1
            self.limit_coordinates()
            self.image_number= np.random.randint(3,6)
        elif action == 2:#up
            self.agent_position_y += 1
            self.limit_coordinates()
            self.image_number= np.random.randint(6,9)
        elif action == 3:#left
            self.agent_position_x += -1
            self.limit_coordinates()
            self.image_number= np.random.randint(9,12)
        
        if self.map[self.agent_position_x,self.agent_position_y]==-1:
            # r = np.random.sample()
            # if r<0.25:
                self.map[self.agent_position_x,self.agent_position_y]=292
                self.total_reset()
        for i,monster in enumerate(self.monsters):
            if self.agent_position_x == monster.map_position.x and self.agent_position_y == monster.map_position.y:
                self.monsters.pop(i)
                self.total_reset()
        
    def transition_probs(self):
        pass

    def change_image(self):
            if self.image_number >= len(self.images)-2:
                self.image_number = 0
            else:
                self.image_number +=1 

