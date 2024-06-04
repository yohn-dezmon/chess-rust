use crate::components::pieces::{BlackPieces, ChessPiece, PieceType, WhitePieces};

// TODO:
// each square needs to have
// (a) chess coordinates (e.g. a1)
// (b) matrix coordinates (e.g. (0, 0)) [done]
// (c) Option<ChessPiece> [done]

pub type ChessBoard = Vec<Vec<Option<&ChessPiece>>>;

pub fn initialize_board() -> ChessBoard {
    let mut board = vec![vec![None; 8]; 8];

    // initialize black pieces into the board
    let black_pieces = BlackPieces::new();

    // a pawn is a Pawn which is a ChessPiece

    // iterate over black pawns
    for pawn in &black_pieces.pawns {
        let row = &pawn.position_xy[0];
        let col = &pawn.position_xy[1];

        board[row][col] = &pawn;
    }

    // initialize white pieces into the board
    let white_pieces = WhitePieces::new();

    for pawn in &white_pieces.pawns {
        let row = &pawn.position_xy[0];
        let col = &pawn.position_xy[1];

        board[row][col] = &pawn;
    }

    board
}

// board[0][0] = SquareContent::Piece(ChessPiece::Pawn);

// TODO: create the dimensions (8x8) I think
