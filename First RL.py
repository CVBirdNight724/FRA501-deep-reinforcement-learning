import numpy as np

class Bandit():
    def __init__(self, mu, sd):
        self.mu = mu
        self.sd = sd
    
    def reward(self):
        return np.random.normal(self.mu, self.sd)


b1 = Bandit(5,2)
b2 = Bandit(10,5)

all_bandits = [b1,b2]
value = [0,0]
n = [0,0]
N = 10000
epsilon = 0.2


for i in range(1,N+1):

    prob = np.random.uniform()
    action = 0

    print("Episode " + str(i))
    print("exploration : " + str(prob))

    if prob < epsilon: #exploration
        action = np.random.randint(2)
    else:
        action = value.index(max(value))

    print("select action: " + str(action))
    print("value 0: " + str(value[0]))
    print("value 1: " + str(value[1]))
    
    reward = all_bandits[action].reward()

    print("reward: " + str(reward))

    n[action] +=1
    
    value[action] = (value[action]*(n[action]-1) + reward)/n[action]

    print("new value 0: " + str(value[0]))
    print("new value 1: " + str(value[1]))
    print()


print(value[0],value[1])