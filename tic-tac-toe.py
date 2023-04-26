from game import TicTacToe,Win_state
from agent import Agent
import cProfile
import os

def main():
    gameplay()

CLEAR_SCREEN = "\x1B[2J"
MOVE_HOME = "\x1B[H"

PRINT_ESC = lambda code: print(code,end="")

class Stats:
    x_wins:int = 0
    o_wins:int = 0
    draws:int = 0
    games_played:int = 0
    move_history:list[list[str]] = []
    def __init__(self):
        return
                  
    def add_game(self,win_state:Win_state):
        if win_state == Win_state.X:
           self.x_wins += 1

        if win_state == Win_state.O:
            self.o_wins += 1

        if win_state == Win_state.DRAW:
            self.draws += 1

        self.games_played += 1

    def print_stats(self):
        PRINT_ESC(CLEAR_SCREEN)
        PRINT_ESC(MOVE_HOME)
        print("x wins: %i, win rate: %f" % (self.x_wins, self.x_wins/self.games_played))
        print("o wins: %i, win rate: %f" % (self.o_wins, self.o_wins/self.games_played))
        print("draws: %i draw rate: %f" % (self.draws,self.draws/self.games_played))
        print("games: %i" % self.games_played)

def print_board(state):
    print("-"*5)
    print("|".join(c or " " for c in state[0:3]))
    print("|".join(c or " " for c in state[3:6]))
    print("|".join(c or " " for c in state[6:9]))
    print("-"*5)
    print("")

def gameplay():
    p1 = Agent("X")
    p2 = Agent("O")
    p1.load_q("X_q_table")
    p2.load_q("O_q_table")
    try:
        games = 0
        current_game = TicTacToe(p1,p2)
        stats = Stats()
        while True:
           state = current_game.step()
           if state != None:
                stats.add_game(state)
                if games % 1000 == 0:
                    stats.print_stats()
                current_game.reset_board()
                games += 1
    except KeyboardInterrupt:
        p1.save_q("X_q_table")
        p2.save_q("O_q_table")



if __name__ == "__main__":
    #for windows 
    os.system("")
    main()
