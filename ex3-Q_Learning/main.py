import gym
import q_library as ql


env = gym.make('CartPole-v0')
bins = ql.create_bins()
episode_lengths, episode_rewards = ql.play_multiple_episode(env, bins, num_episode = 40000, alpha = 0.02, gamma = 0.8, render = True, render_freq = 500)
ql.plot_running_avg(episode_rewards)

    