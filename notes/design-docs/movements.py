# white queen
# movements = {
#     'down': [1,0], # down (row increase)
#     'up': [-1,0], # up (row decrease)
#     'right': [0,1], # right (col increase)
#     'left': [0,-1], # left (col decrease)
#     'up left': [-1, -1], # up left (row and col decrease)
#     'up right': [-1, 1], # up right 
#     'down right': [1, 1], # down right
#     'down left': [1, -1], # down left
# }
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
    if start_coord[0] == end_coord[0] and start_coord[1] == end_coord[1]:
        return 'no movement'

    if end_coord[0] < start_coord[0] and end_coord[1] > start_coord[1]:
        return 'up right'
    if end_coord[0] < start_coord[0] and end_coord[1] < start_coord[1]:
        return 'up left'
    if end_coord[0] < start_coord[0] and end_coord[1] == start_coord[1]:
        return 'up'
    
    if end_coord[0] > start_coord[0] and end_coord[1] > start_coord[1]:
        return 'down right'
    if end_coord[0] > start_coord[0] and end_coord[1] < start_coord[1]:
        return 'down left'
    if end_coord[0] > start_coord[0] and end_coord[1] == start_coord[1]:
        return 'down'
    
    if end_coord[1] > start_coord[1] and end_coord[0] == start_coord[0]:
        return 'right'
    if end_coord[1] < start_coord[1] and end_coord[1] == start_coord[1]:
        return 'left'
    
def in_range(start_coord: list[int], 
             end_coord: list[int], 
             direction: list[int], 
             valid_movements: list[int], 
             move_count: Optional[int]) -> bool:
    if 0 <= end_coord[0] < ROWS and 0 <= end_coord[1] < COLS:
        unit_direction = valid_movements[direction]['unit_direction']
        diffs = [end_coord[0] - start_coord[0], end_coord[1] - start_coord[1]]

        if valid_movements[direction]['unbounded']:
            # At this point we know:
            # 1. the direction is valid
            # 2. the end position is in bounds
            # 3. the piece can move as many pieces in this direction as the board allows

            # but! We still need to check that the diff is in the right ratio 
            # e.g. up two over 1 is invalid for most pieces except for knight.
            unit_direction_increment = unit_direction[:]
            if unit_direction == diffs:
                return True
            while (unit_direction_increment != diffs 
                   and -7 <= unit_direction_increment[0] < ROWS 
                   and -7 <= unit_direction_increment[1] < COLS):
                # update unit_direction_increment by one unit direction 
                unit_direction_increment[0] += unit_direction[0]
                unit_direction_increment[1] += unit_direction[1]

                if unit_direction_increment == diffs:
                    return True
                elif ((unit_direction_increment[0] == diffs[0] and unit_direction_increment[1] != diffs[1]) or 
                    (unit_direction_increment[1] == diffs[1] and unit_direction_increment[0] != diffs[0])
                ):
                    return False
            return False
        else:
            
            # special case for Pawns' first move
            if move_count == 1:
                two_up_or_down = [unit_direction[0]*2, unit_direction[1]]
                return (diffs == unit_direction) or (diffs == two_up_or_down)
            return diffs == unit_direction
    return False


def valid_move(
        start_coord: list[int], 
        end_coord: list[int],
        valid_movements: dict,
        move_count: int = None # in reality, this attribute will only be on Pawns
               ) -> bool:
        """
        valid_movements and start_coord will be part of the Piece object.
        """
        if start_coord == end_coord:
            return False
        direction = get_direction(start_coord, end_coord)
        return (direction in valid_movements and in_range(start_coord, end_coord, direction, valid_movements, move_count))


white_pawn_movements = {
    'up' : {'unbounded': False, 'unit_direction': [-1, 0]},
    'up right': {'unbounded': False, 'unit_direction': [-1, 1]},
    'up left': {'unbounded': False, 'unit_direction': [-1, -1]}
}
print("PAWN testing:")
valid_white_pawn_move = valid_move([6,0], [5,0], white_pawn_movements, 1)
print("Should be true: ")
print(valid_white_pawn_move)

valid_white_pawn_strt_move = valid_move([6, 0], [4, 0], white_pawn_movements, 1)
print("Should be true: ")
print(valid_white_pawn_strt_move)

invalid_white_pawn_2nd_move = valid_move([4, 0], [2, 0], white_pawn_movements, 2)
print("Should be false: ")
print(invalid_white_pawn_2nd_move)

bad_diagonal_first_move = valid_move([6, 0], [4, 2], white_pawn_movements, 1)
print("Should be false: ")
print(bad_diagonal_first_move)

invalid_move = valid_move([6,0], [3,0], white_pawn_movements, 1)
print("Should be false: ")
print(invalid_move)


"""
Knight testing


valid knight movement:
start: [7,1]
end: [5, 2]

invalid knight movement:
start: [7,1]
end: [6,2]
"""
knight_unit_movements = {
    'up right': {'unbounded': False, 'unit_direction': [-2, 1]},
    'up left': {'unbounded': False, 'unit_direction': [-2, -1]},
    'down right': {'unbounded': False, 'unit_direction': [2, 1]},
    'down left': {'unbounded': False, 'unit_direction': [2, -1]},
}
print("\n\n\n")
print("KNIGHT testing:")

valid_knight_move = valid_move([7,1], [5, 2], knight_unit_movements)
print("Should be true: ")
print(valid_knight_move)

invalid_knight_move = valid_move([7,1], [6,2], knight_unit_movements)
print("Should be false: ")
print(invalid_knight_move)


"""
Bishop testing


valid bishop movement:
[7, 2] --> [2, 7]

invalid bishop movement:
[7,2] --> [7, 1]
"""
bishop_unit_movements = {
    'up right': {'unbounded': True, 'unit_direction': [-1, 1]},
    'up left': {'unbounded': True, 'unit_direction': [-1, -1]},
    'down right': {'unbounded': True, 'unit_direction': [1, 1]},
    'down left': {'unbounded': True, 'unit_direction': [1, -1]},
}
print("\n\n\n")
print("BISHOP testing:")

valid_bishop_move = valid_move([7,2], [2, 7], bishop_unit_movements)
print("Should be true: ")
print(valid_bishop_move)

invalid_knight_move = valid_move([7,2], [7,1], bishop_unit_movements)
print("Should be false: ")
print(invalid_knight_move)

invalid_knight_move_v2 = valid_move([7,2], [8,1], bishop_unit_movements)
print("Should be false: ")
print(invalid_knight_move_v2)


"""
Rook testing

"""
rook_unit_movements = {
    'up': {'unbounded': True, 'unit_direction': [-1, 0]},
    'left': {'unbounded': True, 'unit_direction': [0, -1]},
    'right': {'unbounded': True, 'unit_direction': [0, 1]},
    'down': {'unbounded': True, 'unit_direction': [1, 0]},
}
print("\n\n\n")
print("Rook testing:")

valid_rook_move = valid_move([7,0], [0, 0], rook_unit_movements)
print("Should be true: ")
print(valid_bishop_move)

invalid_rook_move = valid_move([0,0], [-1,0], rook_unit_movements)
print("Should be false: ")
print(invalid_rook_move)

invalid_rook_move_v2 = valid_move([7,0], [6,1], rook_unit_movements)
print("Should be false: ")
print(invalid_rook_move_v2)


"""
Queen Testing

"""
queen_unit_movements = {
    'down':{'unbounded': True, 'unit_direction': [1,0]},# down (row increase)
    'up':{'unbounded': True, 'unit_direction': [-1,0]}, # up (row decrease)
    'right':{'unbounded': True, 'unit_direction': [0,1]},# right (col increase)
    'left':{'unbounded': True, 'unit_direction': [0,-1]}, # left (col decrease)
    'up left':{'unbounded': True, 'unit_direction': [-1, -1]}, # up left (row and col decrease)
    'up right':{'unbounded': True, 'unit_direction': [-1, 1]}, # up right 
    'down right':{'unbounded': True, 'unit_direction': [1, 1]}, # down right
    'down left':{'unbounded': True, 'unit_direction': [1, -1]}, # down left
}


print("\n\n\n")
print("QUEEN testing:")

valid_queen_up_left = valid_move([7,3], [4, 0], queen_unit_movements)
print("Should be true: ")
print(valid_queen_up_left)

valid_queen_up_right = valid_move([7,3], [3, 7], queen_unit_movements)
print("Should be true: ")
print(valid_queen_up_left)

valid_queen_down_left = valid_move([3,3], [6, 0], queen_unit_movements)
print("Should be true: ")
print(valid_queen_down_left)

valid_queen_down_right = valid_move([3,3], [7, 7], queen_unit_movements)
print("Should be true: ")
print(valid_queen_down_right)


invalid_queen_oob = valid_move([7,3], [3,8], queen_unit_movements)
print("Should be false: ")
print(invalid_queen_oob)

# import pdb
# pdb.set_trace()
invalid_queen_move_like_knight = valid_move([7,3], [5,4], queen_unit_movements)
print("Should be false: ")
print(invalid_queen_move_like_knight)
