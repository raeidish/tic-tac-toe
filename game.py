import math
import copy

class TicTacToe:
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

    def __init__(self):
        self.initial_state = ["." for _ in range(0,9)]
        self.state = copy.deepcopy(self.initial_state)
        self.move_count = 0
        
    def get_move_count(self):
        return self.move_count

    def get_state(self):
        return self.state
    
    def check_win(self):
        
        for mask in self.WIN_MASKS:
            if(sum([self.state[i] == "X" if x == 1 else False for i,x in enumerate(mask)]) == 3):
                return 1
            if(sum([self.state[i] == "Y" if x == 1 else False for i,x in enumerate(mask)]) == 3):
                return 2

        if(self.move_count == (math.pow(3,2))):
            return 3

        return 0

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
