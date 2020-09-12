# import gym
# import numpy as np


# #------------------------Create an environment--------------------------------------

# env = gym.make('CartPole-v0')
# done = False
# cnt = 0

# #------------------------Reset the environment--------------------------------------

# observation = env.reset()

# #------------------------Running the simulation-------------------------------------

# while not done:

#     env.render()
#     cnt += 1
#     action = env.action_space.sample()
#     observation, reward, done, _ = env.step(action)


import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()