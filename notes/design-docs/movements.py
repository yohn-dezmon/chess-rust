from typing import Optional

ROWS = 8
COLS = 8


def get_direction(start_coord: list[int], end_coord: list[int]) -> str:
    """
    up = end_coord[0] < start_coord[0]
    down = end_coord[0] > start_coord[0]
    right = end_coord[1] > start_coord[1]
    left = end_coord[1] < start_coord[1]
    no_vertical = end_coord[0] == start_coord[0]
    no_horizontal = end_coord[1] == start_coord[1]
    """
    if end_coord[0] < start_coord[0] and end_coord[1] > start_coord[1]:
        return "up right"
    if end_coord[0] < start_coord[0] and end_coord[1] < start_coord[1]:
        return "up left"
    if end_coord[0] < start_coord[0] and end_coord[1] == start_coord[1]:
        return "up"

    if end_coord[0] > start_coord[0] and end_coord[1] > start_coord[1]:
        return "down right"
    if end_coord[0] > start_coord[0] and end_coord[1] < start_coord[1]:
        return "down left"
    if end_coord[0] > start_coord[0] and end_coord[1] == start_coord[1]:
        return "down"

    if end_coord[1] > start_coord[1] and end_coord[0] == start_coord[0]:
        return "right"
    if end_coord[1] < start_coord[1] and end_coord[0] == start_coord[0]:
        return "left"


def in_range(
    start_coord: list[int],
    end_coord: list[int],
    direction: list[int],
    valid_movements: list[int],
    move_count: Optional[int],
) -> bool:
    if 0 <= end_coord[0] < ROWS and 0 <= end_coord[1] < COLS:
        unit_direction = valid_movements[direction]["unit_direction"]
        diffs = [end_coord[0] - start_coord[0], end_coord[1] - start_coord[1]]

        if valid_movements[direction]["unbounded"]:
            # At this point we know:
            # 1. the direction is valid
            # 2. the end position is in bounds
            # 3. the piece can move as many pieces in this direction as the board allows

            # but! We still need to check that the diff is in the right ratio
            # e.g. up two over 1 is invalid for most pieces except for knight.
            unit_direction_increment = unit_direction[:]
            if unit_direction == diffs:
                return True
            while (
                unit_direction_increment != diffs
                and -7 <= unit_direction_increment[0] < ROWS
                and -7 <= unit_direction_increment[1] < COLS
            ):
                # update unit_direction_increment by one unit direction
                unit_direction_increment[0] += unit_direction[0]
                unit_direction_increment[1] += unit_direction[1]

                if unit_direction_increment == diffs:
                    return True
                # TODO: I'm not sure if while we're decreasing from 1 to 0 to -1 if this will run into bugs
                # so make sure we set up a unit test going over a range of x and y values to make sure these
                # 0 cases work as intended
                elif unit_direction[0] == 0:
                    # (right/left)
                    # I'm making these separate inner if statements because I want the above elif to evaluate to true to
                    # prevent hitting the final elif in the event on no lateral or veritcal movement
                    if unit_direction_increment[1] == diffs[1]:
                        return True
                elif unit_direction[1] == 0:
                    # (up/down)
                    if unit_direction_increment[0] == diffs[0]:
                        return True
                elif (
                    unit_direction_increment[0] == diffs[0]
                    and unit_direction_increment[1] != diffs[1]
                ) or (
                    unit_direction_increment[1] == diffs[1]
                    and unit_direction_increment[0] != diffs[0]
                ):
                    # this elif should only get evaluated if neither the x or y unit_direction are 0
                    return False
            return False
        else:
            # special case for Pawns' first move
            if move_count == 1:
                two_up_or_down = [unit_direction[0] * 2, unit_direction[1]]
                return (diffs == unit_direction) or (diffs == two_up_or_down)
            return diffs == unit_direction
    return False


def valid_move(
    start_coord: list[int],
    end_coord: list[int],
    valid_movements: dict,
    move_count: int = None,  # in reality, this attribute will only be on Pawns
) -> bool:
    """
    valid_movements and start_coord will be part of the Piece object.
    """
    if start_coord == end_coord:
        return False
    direction = get_direction(start_coord, end_coord)
    return direction in valid_movements and in_range(
        start_coord, end_coord, direction, valid_movements, move_count
    )


"""
Rook testing

"""
rook_unit_movements = {
    "up": {"unbounded": True, "unit_direction": [-1, 0]},
    "left": {"unbounded": True, "unit_direction": [0, -1]},
    "right": {"unbounded": True, "unit_direction": [0, 1]},
    "down": {"unbounded": True, "unit_direction": [1, 0]},
}
print("\n\n\n")
print("Rook testing:")

valid_rook_move = valid_move([7, 0], [0, 0], rook_unit_movements)
print("Should be true: ")
print(valid_rook_move)

invalid_rook_move = valid_move([0, 0], [-1, 0], rook_unit_movements)
print("Should be false: ")
print(invalid_rook_move)

invalid_rook_move_v2 = valid_move([7, 0], [6, 1], rook_unit_movements)
print("Should be false: ")
print(invalid_rook_move_v2)


"""
Queen Testing

"""
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


print("\n\n\n")
print("QUEEN testing:")

valid_queen_up_left = valid_move([7, 3], [4, 0], queen_unit_movements)
print("Should be true: ")
print(valid_queen_up_left)

valid_queen_up_right = valid_move([7, 3], [3, 7], queen_unit_movements)
print("Should be true: ")
print(valid_queen_up_left)

valid_queen_down_left = valid_move([3, 3], [6, 0], queen_unit_movements)
print("Should be true: ")
print(valid_queen_down_left)

valid_queen_down_right = valid_move([3, 3], [7, 7], queen_unit_movements)
print("Should be true: ")
print(valid_queen_down_right)

valid_queen_up = valid_move([7, 3], [0, 3], queen_unit_movements)
print("Should be true: ")
print(valid_queen_up)

valid_queen_down = valid_move([3, 3], [7, 3], queen_unit_movements)
print("Should be true: ")
print(valid_queen_down)

valid_queen_right = valid_move([7, 3], [7, 4], queen_unit_movements)
print("Should be true right: ")
print(valid_queen_right)

valid_queen_left = valid_move([3, 3], [3, 2], queen_unit_movements)
print("Should be true left: ")
print(valid_queen_left)

invalid_queen_oob = valid_move([7, 3], [3, 8], queen_unit_movements)
print("Should be false: ")
print(invalid_queen_oob)

invalid_queen_move_like_knight = valid_move([7, 3], [5, 4], queen_unit_movements)
print("Should be false: ")
print(invalid_queen_move_like_knight)
