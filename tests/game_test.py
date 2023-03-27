import pytest
from game import TicTacToe
from game import check_win


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
    assert check_win(game.state,game.move_count)

    game.state = ["","","","X","X","X","","",""]
    assert check_win(game.state,game.move_count) == 1
    
    game.state = ["","","","","","","X","X","X"]
    assert check_win(game.state,game.move_count) == 1

    #vertical wins 
    game.state = ["X","","","X","","","X","",""]
    assert check_win(game.state,game.move_count) == 1

    game.state = ["","X","","","X","","","X",""]
    assert check_win(game.state,game.move_count) == 1

    game.state = ["","","X","","","X","","","X"]
    assert check_win(game.state,game.move_count) == 1

    #diagonal wins
    game.state = ["X","","","","X","","","","X"]
    assert check_win(game.state,game.move_count) == 1

    game.state = ["","","X","","X","","X","",""]
    assert check_win(game.state,game.move_count) == 1

def test_y_win(game):
    #horizontal wins
    game.state = ["Y","Y","Y","","","","","",""]
    assert check_win(game.state,game.move_count) == 2

    game.state = ["","","","Y","Y","Y","","",""]
    assert check_win(game.state,game.move_count) == 2
    
    game.state = ["","","","","","","Y","Y","Y"]
    assert check_win(game.state,game.move_count) == 2

    #vertical wins 
    game.state = ["Y","","","Y","","","Y","",""]
    assert check_win(game.state,game.move_count) == 2

    game.state = ["","Y","","","Y","","","Y",""]
    assert check_win(game.state,game.move_count) == 2

    game.state = ["","","Y","","","Y","","","Y"]
    assert check_win(game.state,game.move_count) == 2

    #diagonal wins
    game.state = ["Y","","","","Y","","","","Y"]
    assert check_win(game.state,game.move_count) == 2

    game.state = ["","","Y","","Y","","Y","",""]
    assert check_win(game.state,game.move_count) == 2

def test_draw(game):
    game.move_count = 9
    assert check_win(game.state,game.move_count) == 3

def test_no_win(game):
    assert check_win(game.state,game.move_count) == 0
