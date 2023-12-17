# Components


## Pieces

Maybe I should just have a single struct called `Piece`.
That way I could make a vector of `Piece` for player.

#### Shared Behavior:
- Move
    - from
    - to
- 

### Pawn
* points: 1

### Knight
* points: 3

### Bishop
* points: 3

### Rook
* points: 5

### Queen
* points: 9

### King
* points: null

## Teams

### White
* 8 Pawns
* 2 Knights
* 2 Bishops
* 2 Rooks
* 1 Queen
* 1 King

### Black
* 8 Pawns
* 2 Knights
* 2 Bishops
* 2 Rooks
* 1 Queen
* 1 King


## Board 


## Player

### Player 1
* user_name
* total_points
    - this is the total of all of the player's pieces points
* point_balance
    - this will be how ever many more points this player has than its opponent
    - player_1 total_points - player_2 total_points
    - will only be displayed to user if > 0 
* team
* pieces 
#### methods
* get_total_points()
    - 

### Player 2

