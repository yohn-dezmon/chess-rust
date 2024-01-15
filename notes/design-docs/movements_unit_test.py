import pytest
from movements import get_direction, in_range, valid_move


def test_get_direction() -> None:
    # up right
    res = get_direction([7, 1], [6, 2])
    expected = "up right"
    assert res == expected

    # up left
    res = get_direction([7, 1], [6, 0])
    expected = "up left"
    assert res == expected

    # up
    res = get_direction([7, 1], [6, 1])
    expected = "up"
    assert res == expected

    # down right
    res = get_direction([5, 5], [7, 7])
    expected = "down right"
    assert res == expected

    # down left
    res = get_direction([5, 5], [7, 3])
    expected = "down left"
    assert res == expected

    # down
    res = get_direction([5, 5], [7, 5])
    expected = "down"
    assert res == expected

    # right
    res = get_direction([5, 5], [5, 7])
    expected = "right"
    assert res == expected

    # left
    res = get_direction([5, 5], [5, 4])
    expected = "left"
    assert res == expected


def test_white_pawn_moves() -> None:
    white_pawn_movements = {
        "up": {"unbounded": False, "unit_direction": [-1, 0]},
        "up right": {"unbounded": False, "unit_direction": [-1, 1]},
        "up left": {"unbounded": False, "unit_direction": [-1, -1]},
    }
    # up 1 space first move
    valid_white_pawn_move = valid_move([6, 0], [5, 0], white_pawn_movements, 1)
    assert valid_white_pawn_move

    # up 2 spaces first move
    valid_white_pawn_strt_move = valid_move([6, 0], [4, 0], white_pawn_movements, 1)
    assert valid_white_pawn_strt_move

    invalid_white_pawn_2nd_move = valid_move([4, 0], [2, 0], white_pawn_movements, 2)
    assert not invalid_white_pawn_2nd_move

    bad_diagonal_first_move = valid_move([6, 0], [4, 2], white_pawn_movements, 1)
    assert not bad_diagonal_first_move

    invalid_move = valid_move([6, 0], [3, 0], white_pawn_movements, 1)
    assert not invalid_move


# TODO: implement tests for black pawns
def test_knight_moves():
    knight_unit_movements = {
        "up right": {"unbounded": False, "unit_direction": [-2, 1]},
        "up left": {"unbounded": False, "unit_direction": [-2, -1]},
        "down right": {"unbounded": False, "unit_direction": [2, 1]},
        "down left": {"unbounded": False, "unit_direction": [2, -1]},
    }

    valid_knight_move = valid_move([7, 1], [5, 2], knight_unit_movements)
    assert valid_knight_move

    invalid_knight_move = valid_move([7, 1], [6, 2], knight_unit_movements)
    assert not invalid_knight_move


def test_bishop_moves() -> None:
    bishop_unit_movements = {
        "up right": {"unbounded": True, "unit_direction": [-1, 1]},
        "up left": {"unbounded": True, "unit_direction": [-1, -1]},
        "down right": {"unbounded": True, "unit_direction": [1, 1]},
        "down left": {"unbounded": True, "unit_direction": [1, -1]},
    }

    valid_bishop_move = valid_move([7, 2], [2, 7], bishop_unit_movements)
    assert valid_bishop_move

    invalid_bishop_move = valid_move([7, 2], [7, 1], bishop_unit_movements)
    assert not invalid_bishop_move

    invalid_bishop_move_v2 = valid_move([7, 2], [8, 1], bishop_unit_movements)
    assert not invalid_bishop_move_v2
