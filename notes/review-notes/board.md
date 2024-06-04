# ChessBoard

```rust
// TODO: update type to be &ChessPiece
pub type ChessBoard = Vec<Vec<Option<ChessPiece>>>;
```

- it is a matrix of optional ChessPieces
-


question:
- Should we make it references to the pieces that actually exist in the BlackPieces and WhitePieces instantiations?
    - yes!

