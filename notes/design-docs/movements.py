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


def valid_move(
        start_coord: list[int], 
        end_coord: list[int],
        valid_movements: dict,
        multiplier: bool, 
        color_dir: int = None
               ) -> bool:
    
    """
    
    color_dir: 1 for Black pawns, -1 for white pawns
    multiplier: if true, you can
    """
    direction = get_direction(start_coord, end_coord)





