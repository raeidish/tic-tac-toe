from game import TicTacToe
from time import sleep
import os

CLEAR_SCREEN = "\x1B[2J"
MOVE_HOME = "\x1B[H"

PRINT_ESC = lambda code: print(code,end="")

def print_board(state):
    print("|".join(state[0:3]))
    print("|".join(state[3:6]))
    print("|".join(state[6:9]))

def do_move(game):
    if (game.get_move_count() % 2) == 0:
        prompt = "X turn choose position [1-9]"
        symbol = "X"
    else:
        prompt = "Y turn choose position [1-9]"
        symbol = "Y"

    index = input(prompt)
    index = int(index)-1
    if(index >= 0 and index <= 8):
        valid_move = game.make_move(index, symbol)
        if(valid_move):
            return

    print("Invalid move try again")
    do_move(game)

def check_win_or_draw(win_state):
    match win_state:
        case 0:
            return
        case 1:
            print("X wins!")
        case 2:
            print("Y wins!")
        case 3:
            print("It's a Draw")

def main():
    game = TicTacToe()
    run = True
    while run:
        PRINT_ESC(CLEAR_SCREEN)
        PRINT_ESC(MOVE_HOME)

        print_board(game.get_state())

        win_state = game.check_win()
        if(win_state > 0):
            check_win_or_draw(win_state)
            if(input("press q to quit or any key to reset boad").lower() != "q"):
                game.reset_board()
            else: 
                run = False
        else:
            do_move(game)





if __name__ == "__main__":
    #for windows 
    os.system("")
    main()
