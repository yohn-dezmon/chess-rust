https://docs.google.com/spreadsheets/d/1qN0Tssd3p3CnZIbpjWG9EieZax5c9WN9CRBI9Nbz2a8/edit#gid=0  

I think we should actually store a 2D matrix (vector of vectors). Then within each vector/row, each cell will also be a vector.
The inner vector will typically have one Chess piece, or no chess piece.  
If at some point, one chess piece moves to the same square as an existing piece, then the existing piece will be removed and we'll detect a collision.
At this point the piece being removed can.

I'm not sure we actually need the Black/WhitePieces structs... because those pieces can just be stored within the Board.  
We do need some way to keep track of each team's score... but being able to keep track of which pieces each team has can be done through the board.  


