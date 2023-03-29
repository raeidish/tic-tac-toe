import math
import copy
WIN_MASKS = [
    #horizontal wins
    [1,1,1,0,0,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,1,1,1],
    #vertical wins
    [1,0,0,1,0,0,1,0,0],
    [0,1,0,0,1,0,0,1,0],
    [0,0,1,0,0,1,0,0,1],
    #diagonal wins
    [1,0,0,0,1,0,0,0,1],
    [0,0,1,0,1,0,1,0,0]
]
def check_win(state,move_count):
    for mask in WIN_MASKS:
        if(sum([state[i] == "X" if x == 1 else False for i,x in enumerate(mask)]) == 3):
            return 1
        if(sum([state[i] == "Y" if x == 1 else False for i,x in enumerate(mask)]) == 3):
            return 2

    if(move_count == (math.pow(3,2))):
        return 3
    return 0

def get_available_moves(state):
    #construct all next_possible moves for this iteration
    available_moves = []
    for (i,s) in enumerate(state):
        if s != "X" and s != "Y":
            available_moves.append(i)
    return available_moves

class TicTacToe:
    def __init__(self):
        self.initial_state = ["." for _ in range(0,9)]
        self.state = copy.deepcopy(self.initial_state)
        self.move_count = 0

    def make_move(self,index,symbol):
        #if valid move add in symbol step move_count and return True
        if(self.state[index] != "X" and self.state[index] != "Y"):
            self.state[index] = symbol
            self.move_count += 1
            return True
        #if invalid move return false
        return False

    def reset_board(self):
        self.move_count = 0
        self.state = copy.deepcopy(self.initial_state)
