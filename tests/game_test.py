import pytest
from game import TicTacToe,Win_state

class moc_player:
    move: int = 1
    symbol: str
    win_state: Win_state

    def __init__(self,symbol):
        self.symbol = symbol
    
    def get_move(self,state,available_moves):
        return self.move

    def after_game(self,win_state):
        self.win_state = win_state


@pytest.fixture()
def game():
    p1 = moc_player("X")
    p2 = moc_player("O")
    return TicTacToe(p1,p2)

def test_x_win(game):
    #horizontal wins
    game.state = ["X","X","X","","","","","",""]
    win_state = game.check_win()
    assert win_state == Win_state.X

    game.state = ["","","","X","X","X","","",""]
    win_state = game.check_win()
    assert win_state == Win_state.X
    
    game.state = ["","","","","","","X","X","X"]
    win_state = game.check_win()
    assert win_state == Win_state.X

    #vertical wins 
    game.state = ["X","","","X","","","X","",""]
    win_state = game.check_win()
    assert win_state == Win_state.X

    game.state = ["","X","","","X","","","X",""]
    win_state = game.check_win()
    assert win_state == Win_state.X

    game.state = ["","","X","","","X","","","X"]
    win_state = game.check_win()
    assert win_state == Win_state.X

    #diagonal wins
    game.state = ["X","","","","X","","","","X"]
    win_state = game.check_win()
    assert win_state == Win_state.X

    game.state = ["","","X","","X","","X","",""]
    win_state = game.check_win()
    assert win_state == Win_state.X

def test_moves(game):
    game.players["X"].move = 0
    game.players["O"].move = 1
    game.step()
    assert game.state == ["X","","","","","","","",""]
    game.step()
    assert game.state == ["X","O","","","","","","",""]

def test_o_win(game):
    #horizontal wins
    game.state = ["O","O","O","","","","","",""]
    win_state = game.check_win()
    assert win_state == Win_state.O

    game.state = ["","","","O","O","O","","",""]
    win_state = game.check_win()
    assert win_state == Win_state.O
    
    game.state = ["","","","","","","O","O","O"]
    win_state = game.check_win()
    assert win_state == Win_state.O

    #vertical wins 
    game.state = ["O","","","O","","","O","",""]
    win_state = game.check_win()
    assert win_state == Win_state.O

    game.state = ["","O","","","O","","","O",""]
    win_state = game.check_win()
    assert win_state == Win_state.O

    game.state = ["","","O","","","O","","","O"]
    win_state = game.check_win()
    assert win_state == Win_state.O

    #diagonal wins
    game.state = ["O","","","","O","","","","O"]
    win_state = game.check_win()
    assert win_state == Win_state.O

    game.state = ["","","O","","O","","O","",""]
    win_state = game.check_win()
    assert win_state == Win_state.O

def test_draw(game):
    game.move_count = 9
    win_state = game.check_win()
    assert win_state == Win_state.DRAW

def test_no_win(game):
    assert not game.check_win()
