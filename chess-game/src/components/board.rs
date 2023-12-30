use crate::components::pieces::{BlackPieces, ChessPiece, PieceType, WhitePieces};

// TODO:
// each square needs to have
// (a) chess coordinates (e.g. a1)
// (b) matrix coordinates (e.g. (0, 0)) [done]
// (c) Option<ChessPiece> [done]

// TODO: update type to be &ChessPiece
pub type ChessBoard = Vec<Vec<Option<ChessPiece>>>;

pub fn initialize_board() -> ChessBoard {
    // do I need to make board `mut`? I don't think so.
    let board = vec![vec![None; 8]; 8];

    // initialize black pieces into the board
    let black_pieces = BlackPieces::new();

    // a pawn is a Pawn which is a ChessPiece

    // iterate over black pawns
    for pawn in &black_pieces.pawns {
        let row = &pawn.position_xy[0];
        let col = &pawn.position_xy[1];
        // I think this creates a new instance of the pawn that
        // is stored at this board location
        // so if we need to remove this piece later from a player's pieces,
        // we'll need to use its
        board[row][col] = Some(*pawn);
    }

    // initialize white pieces into the board

    board
}

// board[0][0] = SquareContent::Piece(ChessPiece::Pawn);

// TODO: create the dimensions (8x8) I think
