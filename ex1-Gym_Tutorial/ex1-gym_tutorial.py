import gym
import numpy as np


#------------------------Create an environment--------------------------------------

env = gym.make('CartPole-v0')
done = False
cnt = 0

#------------------------Reset the environment--------------------------------------

observation = env.reset()

#------------------------Running the simulation-------------------------------------

while not done:

    env.render()
    cnt += 1
    action = env.action_space.sample()
    observation, reward, done, _ = env.step(action)