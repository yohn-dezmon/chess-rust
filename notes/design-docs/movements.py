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
    valid_movements: dict,
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




