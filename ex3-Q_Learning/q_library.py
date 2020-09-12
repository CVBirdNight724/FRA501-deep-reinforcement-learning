import gym
import numpy as np 
import matplotlib.pyplot as plt 

MAXSTATES = 10**4

def max_dict(d):
	max_v = float('-inf')
	for key, val in d.items():
		if val > max_v:
			max_v = val
			max_key = key
	return max_key, max_v

def create_bins():	
	bins = np.zeros((4,10))
	bins[0] = np.linspace(-4.8, 4.8, 10)
	bins[1] = np.linspace(-5, 5, 10)
	bins[2] = np.linspace(-.418, .418, 10)
	bins[3] = np.linspace(-5, 5, 10)

	return bins

def assign_bins(observation, bins):
	state = np.zeros(4)
	for i in range(4):
		state[i] = np.digitize(observation[i], bins[i])
	return state

def encode_state(state):
	string_state = ''.join(str(int(e)) for e in state)
	return string_state

def encode_all_state():
	states = []
	for i in range(MAXSTATES):
		states.append(str(i).zfill(4))
	return states

def initialize_Q(env):
	Q = {}

	all_states = encode_all_state()
	for state in all_states:
		Q[state] = {}
		for action in range(env.action_space.n):
			Q[state][action] = 0
	return Q

def play_one_episode(env, bins, Q, eps=0.5, max_step = 500, alpha = 0.01, gamma = 0, render = False):
	observation = env.reset()
	done = False
	step = 0 # number of moves in an episode
	state = encode_state(assign_bins(observation, bins))
	total_reward = 0

	while not done:

		if render:
			env.render()

		step += 1	
		if np.random.uniform() < eps:
			act = env.action_space.sample()
		else:			
			act = max_dict(Q[state])[0]
		
		observation, reward, done, _ = env.step(act)

		total_reward += reward

		if done and step < max_step:
			reward = -300

		state_new = encode_state(assign_bins(observation, bins))

		a1, max_q_next = max_dict(Q[state_new])
		Q[state][act] += alpha*(reward + gamma*max_q_next - Q[state][act])
		state, act = state_new, a1					

	return total_reward, step

def play_multiple_episode(env, bins, num_episode=10000, alpha = 0.01, gamma = 0, render = False, render_freq = 100):
	Q = initialize_Q(env)

	length = []
	reward = []
	for n in range(num_episode):

		if n < 10000:
			eps = 0.25
		else:
			eps = 0.25 / np.sqrt(n+1 - 10000)

		if render and n % render_freq == 0:
			episode_reward, episode_length = play_one_episode(env, bins, Q, eps, alpha = alpha, gamma = gamma, render = True)
		else:
			episode_reward, episode_length = play_one_episode(env, bins, Q, eps, alpha = alpha, gamma = gamma)
		
		if n % 100 == 0:
			print(n, '%.4f' % eps, episode_reward)
		length.append(episode_length)
		reward.append(episode_reward)

	return length, reward

def plot_running_avg(totalrewards):
	N = len(totalrewards)
	running_avg = np.empty(N)
	for t in range(N):
		running_avg[t] = np.mean(totalrewards[max(0, t-100):(t+1)])
	plt.plot(running_avg)
	plt.title("Running Average")
	plt.show()