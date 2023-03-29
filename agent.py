from game import get_available_moves
import random
import json
#made with https://github.com/fcarsten/tic-tac-toe as inspiration
#medium article: https://medium.com/@carsten.friedrich/part-3-tabular-q-learning-a-tic-tac-toe-player-that-gets-better-and-better-fa4da4b0892a
class Agent:
    def __init__(self, alpha = 0.9, gamma=0.95, q_init=0.6,rand_rate=0.7,rand_decay=0.01):
        self.q = {}
        self.history = []
        self.l_rate = alpha
        self.discount = gamma
        self.q_initial_value=q_init
        self.rand_rate=rand_rate
        self.rand_decay=rand_decay

    def get_move(self,state):
        state_string = "".join(state)
        state_hash = state_string
        q_values = self.get_q(state_hash)
        available_moves = get_available_moves(state)       
        """ 
        if random.uniform(0,1) > self.rand_rate:
            move = random.choice(available_moves)
            self.history.append((state_hash,move))
            return move
        """
        while True:
            move = q_values.index(max(q_values))
            if move in available_moves:
                self.history.append((state_hash,move))
                return move
            else:
                q_values[move] = -1.0

    def get_q(self,state_hash):
        if state_hash in self.q:
            return self.q[state_hash]
        else:
            values = [self.q_initial_value for _ in range(9)]
            self.q[state_hash] = values
            return values

    def learning(self,win_state):
        if win_state == 1:
            score = 1.0
        #    if self.rand_rate >= 0.3:
        #        self.rand_rate -= self.rand_decay
        elif win_state == 0:
            score = 0.0
        #    if self.rand_rate < 0.6:
        #        self.rand_rate += self.rand_decay
        else:
            score = 0.5

        # run through the reverse history
        self.history.reverse()
        max_score = -1.0
        for i,state_move in enumerate(self.history):
            q_values = self.get_q(state_move[0])

            if i == 0:
                #set final move to score
                q_values[state_move[1]] = score
            else:
                #apply learning function
                q_values[state_move[1]] = q_values[state_move[1]] * (1.0 - self.l_rate) + self.l_rate * self.discount * max_score

            max_score = max(q_values)
        #reset history for next iteration
        self.history = []

    def save_q(self,location):
        f=open(location,"w")
        f.write(json.dumps(self.q))
