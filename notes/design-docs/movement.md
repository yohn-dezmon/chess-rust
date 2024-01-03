Each piece is going to have a `movements` 
e.g. Pawn has `movements`, and Pawn implements the `Piece` trait.

What happens when a player "moves" a piece?
- they select a piece from a coordinate on the board 
- they select a place on the board where they will move that piece
- when they select a new coordinate, we can check if it is within the valid set of coordinates based on:
a. the current coordinate of the piece
b. the movements accepted for that piece
c. the borders of the board 
d. the movements * unbounded multiplier
    - e.g. a queen can move in any direction (up, down, left, right, and all diagonals)
    - but we then take those singular "movements" and multiply each of them by 

# Unbounded movements

Bishops:
- unbound in up left, up right, down left, down right

Queen:
- unbounded in up, down, right, left, up left, up right, down left, down right 

Rook:
- unbounded in up, right, left, down

