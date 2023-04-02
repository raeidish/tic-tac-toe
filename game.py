import math
import copy

from abc import abstractmethod
from typing import Protocol
from enum import Enum

class Win_state(Enum):
    X = 1,
    O = 2,
    DRAW = 3

class Player(Protocol):
    symbol: str

    @abstractmethod
    def get_move(self,state,available_moves) -> int:
        return NotImplementedError
    
    @abstractmethod
    def after_game(self,win_state) -> None:
        return NotImplementedError


class TicTacToe:
    initial_state: list[str]
    state: list[str]
    move_count: int = 0
    players: dict[str,Player]

    WIN_MASKS: list[list[int]] = [
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

    def __init__(self,player1:Player, player2:Player) -> None:
        self.initial_state = ["" for _ in range(0,9)]
        self.state = copy.copy(self.initial_state)

        if player1.symbol != "X" and player1.symbol != "O":
            raise ValueError("Player 1 has invalid symbol")
        if player2.symbol != "X" and player2.symbol != "O":
            raise ValueError("Player 2 has invalid symbol")
        if player1.symbol == player2.symbol:
            raise ValueError("Players can't have same symbol")

        self.players = {player1.symbol: player1, player2.symbol: player2}

    def step(self):
        #check if win or draw
        win_state = self.check_win()
        if win_state:
            self.players["p1"].after_game(win_state)
            self.players["p2"].after_game(win_state)
            return win_state

        # if x or y turn
        if self.move_count % 2 == 0:
            player = self.players["X"]
        else:
            player = self.players["O"]
        
        available_moves = self.get_available_moves()
        move = player.get_move(self.state,available_moves)
        self.state[move] = player.symbol
        self.move_count += 1
        return None

            

    def reset_board(self):
        self.move_count = 0
        self.state = copy.copy(self.initial_state)

    def check_win(self):
        for mask in self.WIN_MASKS:
            if(sum([self.state[i] == "X" if x == 1 else False for i,x in enumerate(mask)]) == 3):
                return Win_state.X
            if(sum([self.state[i] == "O" if x == 1 else False for i,x in enumerate(mask)]) == 3):
                return Win_state.O

        if(self.move_count == (math.pow(3,2))):
            return Win_state.DRAW
        return None

    def get_available_moves(self):
        #construct all next_possible moves for this iteration
        available_moves = []
        for (i,s) in enumerate(self.state):
            if s != "X" and s != "O":
                available_moves.append(i)
        return available_moves
