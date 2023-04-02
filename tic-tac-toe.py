from game import TicTacToe
from minimax import minimax
from agent import Agent
import os

CLEAR_SCREEN = "\x1B[2J"
MOVE_HOME = "\x1B[H"

PRINT_ESC = lambda code: print(code,end="")

def print_board(state):
    PRINT_ESC(CLEAR_SCREEN)
    PRINT_ESC(MOVE_HOME)
    print("|".join(state[0:3]))
    print("|".join(state[3:6]))
    print("|".join(state[6:9]))

def print_stats(ends):
    PRINT_ESC(CLEAR_SCREEN)
    PRINT_ESC(MOVE_HOME)
    print("x wins: %i" % ends.count("X"))
    print("y wins: %i" % ends.count("Y"))
    print("draws: %i" % ends.count("-"))


def do_move(game,agent):
    if (game.move_count % 2) == 0:
        (index,_) = minimax(game.state,game.move_count,"X",9,True)
        symbol = "X"
    else:
        index = agent.get_move(game.state)
        symbol = "Y"

    if(index >= 0 and index <= 8):
        valid_move = game.make_move(index, symbol)
        if(valid_move):
            return

    do_move(game,agent)

def check_win_or_draw(win_state,agent):
    match win_state:
        case 0:
            return
        case 1:
            agent.learning(0)
            #print("X wins!")
            return("X")
        case 2:
            agent.learning(1)
            #print("Y wins!")
            return("Y")
        case 3:
            agent.learning(2)
            #print("It's a Draw")
            return("-")

def main():
    game = TicTacToe()
    agent = Agent()
    run = True
    
    d = 0
    ends = []
    while run:
        win_state = check_win(game.state,game.move_count)
        if(win_state > 0):
            ends.append(check_win_or_draw(win_state,agent))
            print_stats(ends)
            if d < 200000:
                game.reset_board()
                d += 1
            elif(input("press q to quit or any key to reset boad").lower() != "q"):
                d = 0
                game.reset_board()
            else: 
                agent.save_q("test.json")
                run = False
        else:
            do_move(game,agent)





if __name__ == "__main__":
    #for windows 
    os.system("")
    main()
