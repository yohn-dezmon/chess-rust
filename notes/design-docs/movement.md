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

            How can I check that the diffs simplifies to a unit_direction?
            
            Queen invalid (knight up right):
            up right --> [-1, 1]
            diffs = [-2, 1]
            to get to x, (*2)
            to get to y, (*1)
            is [2,1] in queens unit movements? No.

            Queen valid (up right):
            up right --> [-1, 1]
            diffs = [-4, 4]
            divide diffs by the quotient of diffs/unit direction?


            ok I perhaps have it:
            - if you add unit direction to unit direction X times, does it eventually equal diffs?
            - in other words, if you add unit direction to start, does it eventually equal end?
            - invalid if x or y is > than the diffs x or y BEFORE the corresponding x or y
            - valid if x and y match diffs simultaneously 

            1. figure out how many times x goes into the x and y goes into the y
            e.g. for valid, -1 goes into 4, -4 times, 1 goes into 4, 4 times.
            (what about 0s though?)
            2. check if diffs == unit_direction, if not continue de




                This might have to be different based on (up, down, right, left) and (up right, up left, down right, down left)

                I think what I have currently works for diagonal directions.
                I don't think it works for when one of the unit directions is 0...
                wait uh... it might?

                valid queen down:
                start: [3, 3]
                end: [7, 3]
                diff = [4, 0]
                unit_direction = [1, 0]

                ok the problem is in the elif check, because 0 is already the right y value but x is still incrementing.

                if unit direction x is 0, then only check unit_direction_increment y
                if unit direction y is 0, then only check unit_direction_increment y

# Integrating the logic into the existing Rust code base

- should `valid_movements()` be a function on one of the traits/structs in the `pieces` module?


What is the structure of valid_movements again?
- dict
- 
