import numpy as np
import p5
from settings import *

#TODO base class and ineheritance for different sections
class Agent:
    def __init__(self,nb_row,nb_col,start_position_x,start_position_y,map,monsters,images) -> None:
        self.agent_position = p5.Vector(start_position_x,start_position_y)
        self.agent_start_position = p5.Vector(start_position_x,start_position_y)
        #self.grid = np.zeros(nb_row,nb_col)
        #self.q_values = np.zeros(nb_row,nb_col)
        self.ep_rewards = []
        self.map=map
        self.monsters = monsters
        self.is_visible=False
        self.images = images
        self.image_number = 0

    def set_rewards(self,rewards_position):
        self.rewards_position = rewards_position
    
    def reset(self):
        self.agent_position = self.agent_start_position

    def draw_agent(self,screen_x,screen_y):
        #p5.image_mode(p5.CORNER)
        #p5.fill(255,64,64)
        #p5.ellipse((self.position.x*TILESIZE+10+offset_x,self.position.y*TILESIZE+10+offset_y),TILESIZE-20,TILESIZE-20)
        #p5.ellipse((offset_x,offset_y),TILESIZE,TILESIZE)
        if (not(self.agent_position.x*TILESIZE<screen_x*TILESIZE+WIDTH) or not (self.agent_position.y*TILESIZE<screen_y*TILESIZE+HEIGHT+(-2*TILESIZE))
                or not(self.agent_position.x*TILESIZE>=screen_x*TILESIZE) or not(self.agent_position.y*TILESIZE>=screen_y*TILESIZE)):
                self.is_visible = False
                return
        p5.image(self.images[self.image_number].blend(self.images[self.image_number],"blend"),
            (self.agent_position.x - screen_x) * TILESIZE,(self.agent_position.y - screen_y)*TILESIZE,TILESIZE,TILESIZE)
        self.is_visible = True
   
    def move(self,action):
        # def _limit_coordinates(self, coord):
        #     """
        #     Prevent the agent from falling out of the grid world
        #     :param coord:
        #     :return:
        #     """
        #     coord[0] = min(coord[0], self.shape[0] - 1)
        #     coord[0] = max(coord[0], 0)
        #     coord[1] = min(coord[1], self.shape[1] - 1)
        #     coord[1] = max(coord[1], 0)
        #     return coord
        # Possible actions
        if action == 0:
            self.agent_position += p5.Vector(-1,0)
        elif action == 1:
            self.agent_position += p5.Vector(1,0)
        elif action == 2:
            self.agent_position += p5.Vector(0,1)
        elif action == 3:
            self.agent_position += p5.Vector(0,-1)
        
        reward =-1
        done = False

        if self.map[int(self.agent_position.x),int(self.agent_position.y)]==-1:
            r = np.random.sample()
            if r<0.25:
                reward = -100
                done = True
                self.map[int(self.agent_position.x),int(self.agent_position.y)]=292
        # elif self.agent_position == self.rewards_position:
        #     reward = 0
        #     done = True
        # else:
        #     reward = -1 
        #     done = False
        
        return reward,done
    
    def policy(self):
        action = np.random.randint(0,4)
        return action

    def step(self):
        # def egreedy_policy(q_values, state, epsilon=0.1):
        #     ''' 
        #     Choose an action based on a epsilon greedy policy.    
        #     A random action is selected with epsilon probability, else select the best action.    
        #     '''
        #     if np.random.random() < epsilon:
        #         return np.random.choice(4)
        #     else:
        #         return np.argmax(q_values[state])
        
        # action = egreedy_policy(self.q_values, state)
        # # Do the action
        # next_state, reward, done = self.move(action)
        # reward_sum += reward
        # # Update q_values       
        # td_target = reward + 0.9 * np.max(self.q_values[next_state])
        # td_error = td_target - self.q_values[state][action]
        # self.q_values[state][action] += learning_rate * td_error
        # # Update state
        # state = next_state
        # print(state)
        # self.ep_rewards.append(reward_sum)
        reward , done = self.move(self.policy())
        if not done:
            pass
        else:
            self.reset()

    def transition_probs(self):
        pass

    def change_image(self):
            if self.image_number >= len(self.images)-1:
                self.image_number = 0
            else:
                self.image_number +=1 
