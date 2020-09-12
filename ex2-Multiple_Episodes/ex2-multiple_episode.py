import gym
import numpy as np

def play_one_episode(env, render = False, maxStep = 10000):
    done = False
    cnt = 0
    action_sequence = []

    observation = env.reset()

    while not done:
        if render:
            env.render()
        cnt += 1
        action = env.action_space.sample()
        action_sequence.append(action)
        observation, reward, done, _ = env.step(action)

        if cnt > maxStep:
            break
    
    return action_sequence,cnt


env = gym.make('CartPole-v0')

for i in range(100):
    play_one_episode(env, render = True)

    