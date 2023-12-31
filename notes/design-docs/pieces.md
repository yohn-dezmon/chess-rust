Diagram: https://docs.google.com/drawings/d/1Yl4QXWbwGiyM827-5eQa9BcXNqpx25d9qp-zN0rSBfE/edit


I'm not sure how I should instantiate movements because it is sort of the same for each PieceType, but the direction will be different (e.g. Black pawns move down the board, White pawns move up teh board.)




ChessPiece:
- PieceType
    - points
    - movements
- position_xy
- position_text
- Color
    - direction (basically indicates if pieces can move up or down the board, for some pieces this won't end up being used)



