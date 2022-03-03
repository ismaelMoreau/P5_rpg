import numpy as np
class Agent:
    def __init__(self,nb_row,nb_col,start_position) -> None:
        self.agent_position = start_position
        self.agent_start_position = start_position
        self.grid = np.zeros(nb_row,nb_col)
        self.q_values = np.zeros(nb_row,nb_col)
        self.ep_rewards = []

    def set_rewards(self,rewards_position):
        self.rewards_position = rewards_position
    
    def reset(self):
        self.agent_position = self.agent_start_position


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
        if action == 0 and self.agent_position[0] > 0:
            self.agent_position = (self.agent_position[0] - 1, self.agent_position[1])
        elif action == 1 and self.agent_position[0] < self.grid.shape[0]:
            self.agent_position = (self.agent_position[0] + 1, self.agent_position[1])
        elif action == 2 and self.agent_position[1] < self.grid.shape[1]:
            self.agent_position = (self.agent_position[0], self.agent_position[1] + 1)
        elif action == 3 and self.agent_position[1] > 0:
            self.agent_position = (self.agent_position[0], self.agent_position[1] - 1)
        
        if self.agent_position == self.rewards_position:
            reward = 0
            done = True
        else:
            reward = -1 
            done = False
        
        return reward,done

    def step(self):
        def egreedy_policy(q_values, state, epsilon=0.1):
            ''' 
            Choose an action based on a epsilon greedy policy.    
            A random action is selected with epsilon probability, else select the best action.    
            '''
            if np.random.random() < epsilon:
                return np.random.choice(4)
            else:
                return np.argmax(q_values[state])
        
        action = egreedy_policy(self.q_values, state)
        # Do the action
        next_state, reward, done = self.move(action)
        reward_sum += reward
        # Update q_values       
        td_target = reward + 0.9 * np.max(self.q_values[next_state])
        td_error = td_target - self.q_values[state][action]
        self.q_values[state][action] += learning_rate * td_error
        # Update state
        state = next_state
        print(state)
        self.ep_rewards.append(reward_sum)

    def transition_probs(self):
        pass

