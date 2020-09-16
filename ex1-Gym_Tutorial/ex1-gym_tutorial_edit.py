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
    
    def chooseAction(self):

#------------------------Running the simulation-------------------------------------
state = 0
# while not done:
for i in range(1000):

    env.render()
    cnt += 1
    #---------------------Perform Action---------------------#
    # action = env.action_space.sample()
    if 

    #---------------------Environment---------------------#
    observation, reward, done, _ = env.step(action)
    x, d_x, q, d_q = observation

    # print("action: ", action)
    # print("observation: ", observation)
    # print("reward: ", reward)

    time.sleep(0.3)

env.close

