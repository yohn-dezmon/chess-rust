# should I create a board?

# white queen
movements = {
    'down': [1,0], # down (row increase)
    'up': [-1,0], # up (row decrease)
    'right': [0,1], # right (col increase)
    'left': [0,-1], # left (col decrease)
    'up left': [-1, -1], # up left (row and col decrease)
    'up right': [-1, 1], # up right 
    'down right': [1, 1], # down right
    'down left': [1, -1], # down left
}

starting_coord = [7,3]

move_to = [4, 6]

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
    
def in_range(start_coord, end_coord, direction, valid_movements, move_count) -> bool:
    """
    A rook's movements are valid if it only changes in either row or column.
    i.e. the unbounded multiplier is specific to one location at a time.
    at this point we know the direction, so it can be unbounded in THAT direction.

    White Pawn:
    valid: 
        - start: [6,0]
        - end:   [5,0]
        - diff row: -1
        - diff col: 0 
        - unit_direction: [-1, 0] (up)

        
    invalid:
        - start: [6,0]
        - end: []
    """

    unit_direction = movements[direction]
    diffs = [end_coord[0] - start_coord[0], end_coord[1] - start_coord[1]]

    if valid_movements[direction]['unbounded']:
        pass
    else:
        # special case for Pawns' first move
        # TODO: check that this evaluates correctly for diagonal movements!
        if move_count == 1:
            two_up_or_down = [unit_direction[0]*2, unit_direction[1]]
            return (diffs == unit_direction) or (diffs == two_up_or_down)
        return diffs == unit_direction

"""
valid_movements and start_coord will be part of the Piece object.
"""
def valid_move(
        start_coord: list[int], 
        end_coord: list[int],
        valid_movements: dict,
        move_count: int = None # in reality, this attribute will only be on Pawns
               ) -> bool:
    """
    color_dir: 1 for Black pawns, -1 for white pawns
    multiplier: if true, you can
    """
    direction = get_direction(start_coord, end_coord)
    return (direction in valid_movements and in_range(start_coord, end_coord, direction, valid_movements, move_count))

# aw crap, pawns can move up two only on the first move from their original position
# gah, encoding that is going to suck.
white_pawn_movements = {
    'up' : {'unbounded': False},
    'up right': {'unbounded': False},
    'up left': {'unbounded': False}
}

# white pawns
# oh snap they can move diagonally if attacking!
# white_pawn_movements = set('up', 'up right', 'up left')
white_pawn_multiplier = 1

good_move = valid_move([6,0], [5,0], white_pawn_movements, 1)
print("Should be true: ")
print(good_move)

good_first_move = valid_move([6, 0], [4, 0], white_pawn_movements, 1)
print("Should be true: ")
print(good_move)

bad_diagonal_first_move = valid_move([6, 0], [4, 2], white_pawn_movements, 1)
print("Should be false: ")
print(bad_diagonal_first_move)

invalid_move = valid_move([6,0], [3,0], white_pawn_movements, 1)
print("Should be false: ")
print(invalid_move)

