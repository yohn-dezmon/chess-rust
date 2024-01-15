import pytest
from movements import get_direction, valid_move


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


def test_rook_moves() -> None:
    rook_unit_movements = {
        "up": {"unbounded": True, "unit_direction": [-1, 0]},
        "left": {"unbounded": True, "unit_direction": [0, -1]},
        "right": {"unbounded": True, "unit_direction": [0, 1]},
        "down": {"unbounded": True, "unit_direction": [1, 0]},
    }

    valid_rook_move = valid_move([7, 0], [0, 0], rook_unit_movements)
    assert valid_rook_move

    invalid_rook_move = valid_move([0, 0], [-1, 0], rook_unit_movements)
    assert not invalid_rook_move

    invalid_rook_move_v2 = valid_move([7, 0], [6, 1], rook_unit_movements)
    assert not invalid_rook_move_v2


def test_queen_moves() -> None:
    queen_unit_movements = {
        "down": {"unbounded": True, "unit_direction": [1, 0]},  # down (row increase)
        "up": {"unbounded": True, "unit_direction": [-1, 0]},  # up (row decrease)
        "right": {"unbounded": True, "unit_direction": [0, 1]},  # right (col increase)
        "left": {"unbounded": True, "unit_direction": [0, -1]},  # left (col decrease)
        "up left": {
            "unbounded": True,
            "unit_direction": [-1, -1],
        },  # up left (row and col decrease)
        "up right": {"unbounded": True, "unit_direction": [-1, 1]},  # up right
        "down right": {"unbounded": True, "unit_direction": [1, 1]},  # down right
        "down left": {"unbounded": True, "unit_direction": [1, -1]},  # down left
    }
    valid_queen_up_left = valid_move([7, 3], [4, 0], queen_unit_movements)
    assert valid_queen_up_left

    valid_queen_up_right = valid_move([7, 3], [3, 7], queen_unit_movements)
    assert valid_queen_up_right

    valid_queen_down_left = valid_move([3, 3], [6, 0], queen_unit_movements)
    assert valid_queen_down_left

    valid_queen_down_right = valid_move([3, 3], [7, 7], queen_unit_movements)
    assert valid_queen_down_right

    valid_queen_up = valid_move([7, 3], [0, 3], queen_unit_movements)
    assert valid_queen_up

    valid_queen_down = valid_move([3, 3], [7, 3], queen_unit_movements)
    assert valid_queen_down

    valid_queen_right = valid_move([7, 3], [7, 4], queen_unit_movements)
    assert valid_queen_right

    valid_queen_left = valid_move([3, 3], [3, 2], queen_unit_movements)
    assert valid_queen_left

    invalid_queen_oob = valid_move([7, 3], [3, 8], queen_unit_movements)
    assert not invalid_queen_oob

    invalid_queen_move_like_knight = valid_move([7, 3], [5, 4], queen_unit_movements)
    assert not invalid_queen_move_like_knight
