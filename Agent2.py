import numpy as np








class Agent2:
    terrain_color = dict(normal=[127/360, 0, 96/100],
                         objective=[26/360, 100/100, 100/100],
                         cliff=[247/360, 92/100, 70/100],
                         player=[344/360, 93/100, 100/100])
 

    def __init__(self):
        self.player = None
        self._create_grid()  
        
    def _create_grid(self, initial_grid=None):
        self.grid = self.terrain_color['normal'] * np.ones((4, 12, 3))
        self._add_objectives(self.grid)
        
    def _add_objectives(self, grid):
        grid[-1, 1:11] = self.terrain_color['cliff']
        grid[-1, -1] = self.terrain_color['objective']
        
        
    def reset(self):
        self.player = (3, 0)        
        return self._position_to_id(self.player)
    
    def step(self, action):
        # Possible actions
        if action == 0 and self.player[0] > 0:
            self.player = (self.player[0] - 1, self.player[1])
        if action == 1 and self.player[0] < 3:
            self.player = (self.player[0] + 1, self.player[1])
        if action == 2 and self.player[1] < 11:
            self.player = (self.player[0], self.player[1] + 1)
        if action == 3 and self.player[1] > 0:
            self.player = (self.player[0], self.player[1] - 1)
            
        # Rules
        if all(self.grid[self.player] == self.terrain_color['cliff']):
            reward = -100
            done = True
        elif all(self.grid[self.player] == self.terrain_color['objective']):
            reward = 0
            done = True
        else:
            reward = -1
            done = False
            
        return self._position_to_id(self.player), reward, done
    
    def _position_to_id(self, pos):
        ''' Maps a position in x,y coordinates to a unique ID '''
        return pos[0] * 12 + pos[1]
    
    def _id_to_position(self, idx):
        return (idx // 12), (idx % 12)

def test():


        env = Agent2()


        # The number of states in simply the number of "squares" in our grid world, in this case 4 * 12
        num_states = 4 * 12
        # We have 4 possible actions, up, down, right and left
        num_actions = 4

        q_values = np.zeros((num_states, num_actions))
        UP = 0
        DOWN = 1
        RIGHT = 2
        LEFT = 3
        actions = ['UP', 'DOWN', 'RIGHT', 'LEFT']


        def egreedy_policy(q_values, state, epsilon=0.1):
                ''' 
                Choose an action based on a epsilon greedy policy.    
                A random action is selected with epsilon probability, else select the best action.    
                '''
                if np.random.random() < epsilon:
                        return np.random.choice(4)
                else:
                        return np.argmax(q_values[state])

        def q_learning(env, num_episodes=500, exploration_rate=0.1,
                learning_rate=0.5, gamma=0.9):    
                q_values = np.zeros((num_states, num_actions))
                ep_rewards = []

                for _ in range(num_episodes):
                        state = env.reset()    
                        done = False
                        reward_sum = 0

                        while not done:            
                                # Choose action        
                                action = egreedy_policy(q_values, state, exploration_rate)
                                # Do the action
                                next_state, reward, done = env.step(action)
                                reward_sum += reward
                                # Update q_values       
                                td_target = reward + 0.9 * np.max(q_values[next_state])
                                td_error = td_target - q_values[state][action]
                                q_values[state][action] += learning_rate * td_error
                                # Update state
                                state = next_state
                                print(state)
                        ep_rewards.append(reward_sum)

                return ep_rewards, q_values
