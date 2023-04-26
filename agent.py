from copy import copy
from game import Win_state
import json
import random
import copy
#made with https://github.com/fcarsten/tic-tac-toe as inspiration
#medium article: https://medium.com/@carsten.friedrich/part-3-tabular-q-learning-a-tic-tac-toe-player-that-gets-better-and-better-fa4da4b0892a
class Agent:
    symbol:str
    q:dict[str,list[float]] = {}
    history:list[tuple[str,int]] = []
    learn_rate:float = 0.8
    discount:float = 0.7
    initial_q:float = 0.6
    
    rand_rate:float = 0.6
    rand_decay:float = 0.001
    def __init__(self,symbol):
        self.symbol = symbol
        return

    def get_move(self,state,available_moves):
        state_string = "".join(state)
        state_hash = state_string
        q_values = self.get_q(state_hash)

        if random.uniform(0,1) > self.rand_rate:
            try:
                move = random.choice(available_moves)
                self.history.append((state_hash,move))
                return move
            except:
                print(state)
                print(available_moves)

        while True:
            move = q_values.index(max(q_values))
            if move in available_moves:
                self.history.append((state_hash,move))
                return move
            else:
                q_values[move] -= 0.1

    def get_q(self,state_hash):
        if state_hash in self.q:
            return copy.copy(self.q[state_hash])
        else:
            values = [random.uniform(0,1) for _ in range(9)]
            self.q[state_hash] = values
            return self.q[state_hash]

    def after_game(self,win_state:Win_state):
        random.seed()
        score = 0.0
        if  self.symbol == "X" and win_state == Win_state.X:
            if win_state == Win_state.X:
                score = 1.0
            elif win_state == Win_state.O:
                score = 0.0
        elif self.symbol == "O": 
            if win_state == Win_state.O:
                score = 1.0
            elif win_state == Win_state.X:
                score = -1.0
        elif win_state == Win_state.DRAW:
            score = 0.5

        if score > 0.9 and self.rand_rate > 0.05:
            self.rand_rate -= self.rand_decay
        elif score < 0.5 and self.rand_rate < 0.20:
            self.rand_rate += self.rand_decay
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
                q_values[state_move[1]] = q_values[state_move[1]] * (1.0 - self.learn_rate) + self.learn_rate * self.discount * max_score

            max_score = max(q_values)
        #reset history for next iteration
        self.history = []

    def save_q(self,location):
        f=open(location,"w")
        f.write(json.dumps(self.q))
    def load_q(self,location):
        f=open(location,"r")
        self.q = json.load(f)
