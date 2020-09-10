import numpy as np

class SlotMachine:
    def __init__(self, mu, sd):
        self.MU = mu
        self.SD = sd
    def reward(self):
        return np.random.normal(self.MU, self.SD)

class Environment:
    def __init__(self):
        Slot1 = SlotMachine(11,2)
        Slot2 = SlotMachine(10, 1.4)
        Slot3 = SlotMachine(11, 3)    
        self.slot = [Slot1, Slot2, Slot3]
    def numberSlot(self):
        return len(self.slot)
    def getReward(self, action):
        return self.slot[action].reward()

class Agent:
    def __init__(self):
        env = Environment()
        nSlot = env.numberSlot()
        self.policy = list(range(nSlot))
        self.q_val = np.zeros((1, nSlot))
        self.nAction = np.zeros(len(self.policy))
        self.reward = np.zeros(1)
        self.t = 0
    def epsilonGreedy(self, epsilon=0.3):
        prob = np.random.uniform()   
        if prob < epsilon:
            A = np.random.randint(0, len(self.policy))
        else:
            A = np.argmax(self.q_val[self.t])
        return A
    def UCB(self, c=1/np.sqrt(2)):
        Q = self.q_val[self.t]
        U = c*np.sqrt(np.log(self.t)/self.nAction)
        return np.argmax(Q+U)
    def update(self, action, reward):
        self.nAction[action] += 1
        Q = [self.q_val[self.t]]
        q = (reward + (self.nAction[action]-1)*self.q_val[self.t][action])/self.nAction[action]
        Q[0][action] = q
        self.q_val = np.concatenate((self.q_val, Q), axis=0)
        self.reward = np.concatenate((self.reward, np.array([reward])))
        self.t += 1
        return Q[0]


Env = Environment()
ag = Agent()
# epsilon = 0.1
# c = 0.1
n = 10000

if __name__ == "__main__":
    for i in range(1, n+1):
        if i > 300:
            action = ag.UCB()
        else:
            action = ag.epsilonGreedy()
        reward = Env.getReward(action)
        actionValue = ag.update(action, reward)

        print("Gen", i)
        print("Choose: ", action)
        print("Reward: ", reward)
        print("new Value0: ", actionValue[0])
        print("new Value1: ", actionValue[1])
        print("new Value2: ", actionValue[2])
        print()
    print(ag.nAction)