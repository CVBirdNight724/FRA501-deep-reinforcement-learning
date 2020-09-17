import gym
import numpy as np
import time

#------------------------Create an environment--------------------------------------

env = gym.make('CartPole-v0')
done = False
cnt = 0

#------------------------Reset the environment--------------------------------------

observation = env.reset()

#------------------------Create the Agent-------------------------------------------

class Agent:
    def __init__(self):
        self.policy = [0, 1] # 0 is left ,1 is right
        self.state = 0
    
    # def chooseAction(self):

#------------------------Running the simulation-------------------------------------
"""
state=0 perform q<0
state=1 perform q>0
"""


# while not done:
state = 0
for i in range(1000):

    env.render()
    cnt += 1
    #---------------------Perform Action---------------------#
    # action = env.action_space.sample()
    if state == 0:
        action = 0
    else:
        action = 1
    #---------------------Environment---------------------#
    observation, reward, done, _ = env.step(action)
    x, d_x, q, d_q = observation

    if q > 0 and d_x <= 1:
        state = 1
    else:
        state = 0
    print("action: ", action)
    print("observation: ", observation)
    print("state: ", state)
    print("reward: ", reward)

    # time.sleep(0.3)

env.close

