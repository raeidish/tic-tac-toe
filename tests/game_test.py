import pytest
from game import TicTacToe


@pytest.fixture()
def game():
    return TicTacToe()

def test_invalid_move(game):
    game.state = ["X","Y","","","","","","",""]
    assert not game.make_move(0,"X")

def test_valid_move(game):
    game.state = ["X","Y","","","","","","",""]
    assert game.make_move(2,"X")

def test_x_win(game):
    #horizontal wins
    game.state = ["X","X","X","","","","","",""]
    assert game.check_win() == 1

    game.state = ["","","","X","X","X","","",""]
    assert game.check_win() == 1
    
    game.state = ["","","","","","","X","X","X"]
    assert game.check_win() == 1

    #vertical wins 
    game.state = ["X","","","X","","","X","",""]
    assert game.check_win() == 1

    game.state = ["","X","","","X","","","X",""]
    assert game.check_win() == 1

    game.state = ["","","X","","","X","","","X"]
    assert game.check_win() == 1

    #diagonal wins
    game.state = ["X","","","","X","","","","X"]
    assert game.check_win() == 1

    game.state = ["","","X","","X","","X","",""]
    assert game.check_win() == 1

def test_y_win(game):
    #horizontal wins
    game.state = ["Y","Y","Y","","","","","",""]
    assert game.check_win() == 2

    game.state = ["","","","Y","Y","Y","","",""]
    assert game.check_win() == 2
    
    game.state = ["","","","","","","Y","Y","Y"]
    assert game.check_win() == 2

    #vertical wins 
    game.state = ["Y","","","Y","","","Y","",""]
    assert game.check_win() == 2

    game.state = ["","Y","","","Y","","","Y",""]
    assert game.check_win() == 2

    game.state = ["","","Y","","","Y","","","Y"]
    assert game.check_win() == 2

    #diagonal wins
    game.state = ["Y","","","","Y","","","","Y"]
    assert game.check_win() == 2

    game.state = ["","","Y","","Y","","Y","",""]
    assert game.check_win() == 2

def test_draw(game):
    game.move_count = 9
    assert game.check_win() == 3

def test_no_win(game):
    assert game.check_win() == 0
