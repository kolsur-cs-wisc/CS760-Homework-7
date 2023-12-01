import gym
from gym import spaces

class CustomMDP(gym.Env):
    name = "CustomMDP"
    def __init__(self):
        self.states = ['A', 'B']
        self.actions = {0 : 'move', 1 : 'stay'}
        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Discrete(2)
        self.gamma = 0.8
        self.rewards = {'move' : 0, 'stay' : 1}
        self.state = 'A'
        self.transition = {'A' : {'move' : 'B', 'stay' : 'A'}, 'B' : {'move' : 'A', 'stay' : 'B'}}

    def reset(self):
        self.state = 'A'
        return self.state

    def step(self, action):
        next_state = self.transition[self.state][self.actions[action]]
        reward = self.rewards[self.actions[action]]
        self.state = next_state

        return self.state, reward, False, {}