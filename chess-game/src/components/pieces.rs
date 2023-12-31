use crate::components::color::Color;

#[derive(Debug, Clone, Copy)]
pub enum PieceType {
    Pawn,
    Knight,
    Bishop,
    Rook,
    Queen,
    King,
}

#[derive(Debug)]
pub struct ChessPiece {
    piece_type: PieceType,
    color: Color,
    position_xy: Vec<i32>,
    position_text: String, // using String bc this will update throughout the game
    start_position_id: String,
}

pub struct ChessPieces {
    pawns: Vec<ChessPiece>,
    knights: Vec<ChessPiece>,
    bishops: Vec<ChessPiece>,
    rooks: Vec<ChessPiece>,
    queen: Vec<ChessPiece>, // I made this a vector so we can remove pieces as the game progresses
    king: Vec<ChessPiece>,
}

pub struct BlackPieces {
    pieces: ChessPieces,
}

const LETTERS: [char; 8] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];

impl BlackPieces {
    pub fn new() -> Self {
        let mut pawns = Vec::new();
        // for letter in LETTERS {
        // can I make this same call later? or does this consume LETTERS?
        let mut letter_iter = LETTERS.iter();

        for col in 0..8 {
            if let Some(letter) = letter_iter.next() {
                let piece = ChessPiece {
                    piece_type: PieceType::Pawn,
                    color: Color::Black,
                    position_xy: vec![1, col],
                    position_text: format!("{}7", letter),
                    start_position_id: format!("{}7", letter),
                };
                pawns.push(piece);
            } else {
                break;
            }
        }
        // }

        let mut knights = Vec::new();
        let knight_left = ChessPiece {
            piece_type: PieceType::Knight,
            color: Color::Black,
            position_xy: vec![0, 1],
            position_text: String::from("b8"),
            start_position_id: String::from("b8"),
        };
        let knight_right = ChessPiece {
            piece_type: PieceType::Knight,
            color: Color::Black,
            position_xy: vec![0, 6],
            position_text: String::from("g8"),
            start_position_id: String::from("g8"),
        };
        knights.push(knight_left);
        knights.push(knight_right);

        let mut bishops = Vec::new();
        let bishop_left = ChessPiece {
            piece_type: PieceType::Bishop,
            color: Color::Black,
            position_xy: vec![0, 2],
            position_text: String::from("c8"),
            start_position_id: String::from("c8"),
        };
        let bishop_right = ChessPiece {
            piece_type: PieceType::Bishop,
            color: Color::Black,
            position_xy: vec![0, 5],
            position_text: String::from("f8"),
            start_position_id: String::from("f8"),
        };
        bishops.push(bishop_left);
        bishops.push(bishop_right);

        let mut rooks = Vec::new();
        let rook_left = ChessPiece {
            piece_type: PieceType::Rook,
            color: Color::Black,
            position_xy: vec![0, 0],
            position_text: String::from("a8"),
            start_position_id: String::from("a8"),
        };
        let rook_right = ChessPiece {
            piece_type: PieceType::Rook,
            color: Color::Black,
            position_xy: vec![0, 7],
            position_text: String::from("h8"),
            start_position_id: String::from("h8"),
        };
        rooks.push(rook_left);
        rooks.push(rook_right);

        let mut queen = vec![ChessPiece {
            piece_type: PieceType::Queen,
            color: Color::Black,
            position_xy: vec![0, 3],
            position_text: String::from("d8"),
            start_position_id: String::from("d8"),
        }];

        let mut king = vec![ChessPiece {
            piece_type: PieceType::King,
            color: Color::Black,
            position_xy: vec![0, 4],
            position_text: String::from("e8"),
            start_position_id: String::from("e8"),
        }];

        BlackPieces {
            pieces: ChessPieces {
                // Field init shorthand!
                pawns,
                knights,
                bishops,
                rooks,
                queen,
                king,
            },
        }
    }
}

pub struct WhitePieces {
    pieces: ChessPieces,
}

impl WhitePieces {
    pub fn new() -> Self {
        let mut pawns = Vec::new();
        let mut letter_iter = LETTERS.iter();

        for col in 0..8 {
            if let Some(letter) = letter_iter.next() {
                let piece = ChessPiece {
                    piece_type: PieceType::Pawn,
                    color: Color::White,
                    position_xy: vec![6, col],
                    position_text: format!("{}2", letter),
                    start_position_id: format!("{}2", letter),
                };
                pawns.push(piece);
            } else {
                break;
            }
        }

        let mut knights = Vec::new();
        let knight_left = ChessPiece {
            piece_type: PieceType::Knight,
            color: Color::White,
            position_xy: vec![7, 1],
            position_text: String::from("b1"),
            start_position_id: String::from("b1"),
        };
        let knight_right = ChessPiece {
            piece_type: PieceType::Knight,
            color: Color::White,
            position_xy: vec![7, 6],
            position_text: String::from("g1"),
            start_position_id: String::from("g1"),
        };
        knights.push(knight_left);
        knights.push(knight_right);

        let mut bishops = Vec::new();
        let bishop_left = ChessPiece {
            piece_type: PieceType::Bishop,
            color: Color::White,
            position_xy: vec![7, 2],
            position_text: String::from("c1"),
            start_position_id: String::from("c1"),
        };
        let bishop_right = ChessPiece {
            piece_type: PieceType::Bishop,
            color: Color::White,
            position_xy: vec![7, 5],
            position_text: String::from("f1"),
            start_position_id: String::from("f1"),
        };
        bishops.push(bishop_left);
        bishops.push(bishop_right);

        let mut rooks = Vec::new();
        let rook_left = ChessPiece {
            piece_type: PieceType::Rook,
            color: Color::White,
            position_xy: vec![7, 0],
            position_text: String::from("a1"),
            start_position_id: String::from("a1"),
        };
        let rook_right = ChessPiece {
            piece_type: PieceType::Rook,
            color: Color::White,
            position_xy: vec![7, 7],
            position_text: String::from("h1"),
            start_position_id: String::from("h1"),
        };
        rooks.push(rook_left);
        rooks.push(rook_right);

        let mut queen = vec![ChessPiece {
            piece_type: PieceType::Queen,
            color: Color::White,
            position_xy: vec![7, 3],
            position_text: String::from("d1"),
            start_position_id: String::from("d1"),
        }];

        let mut king = vec![ChessPiece {
            piece_type: PieceType::King,
            color: Color::White,
            position_xy: vec![7, 4],
            position_text: String::from("e1"),
            start_position_id: String::from("e1"),
        }];

        WhitePieces {
            pieces: ChessPieces {
                // Field init shorthand!
                pawns,
                knights,
                bishops,
                rooks,
                queen,
                king,
            },
        }
    }
}

pub trait Piece {
    // fn move(&self);

    fn get_points(&self) -> i32;

    // fn get_directed_movements(&self, piece: ChessPiece) -> Vec<Vec<i32>>;
}

#[derive(Debug)]
pub struct Pawn {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for Pawn {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Pawn {
    pub fn new() -> Self {
        // set default value to 1 for Pawn
        Pawn {
            points: 1,
            // this is later combined with direction
            movements: vec![vec![1, 0]],
        }
    }
}

#[derive(Debug)]
pub struct Knight {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for Knight {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Knight {
    pub fn new() -> Self {
        Knight {
            points: 3,
            movements: vec![vec![-2, 1], vec![-2, -1], vec![2, 1], vec![2, -1]],
        }
    }
}

#[derive(Debug)]
pub struct Bishop {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for Bishop {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Bishop {
    pub fn new() -> Self {
        Bishop {
            points: 3,
            // TODO: figure out how to implement unbounded movements
            movements: vec![vec![]],
        }
    }
}

#[derive(Debug)]
pub struct Rook {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for Rook {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Rook {
    pub fn new() -> Self {
        Rook {
            points: 5,
            movements: vec![vec![]],
        }
    }
}

#[derive(Debug)]
pub struct Queen {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for Queen {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Queen {
    pub fn new() -> Self {
        Queen {
            points: 9,
            movements: vec![vec![]],
        }
    }
}

#[derive(Debug)]
pub struct King {
    points: i32,
    movements: Vec<Vec<i32>>,
}

impl Piece for King {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl King {
    pub fn new() -> Self {
        King {
            points: 0,
            movements: vec![vec![1, 0], vec![-1, 0], vec![0, 1], vec![0, -1]],
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn black_pieces_instantiation() {
        let black_pieces = BlackPieces::new();
        assert_eq!(black_pieces.pieces.pawns.len(), 8);
        assert_eq!(
            &black_pieces.pieces.pawns[0].position_text,
            &String::from("a7")
        );
    }

    #[test]
    fn white_pieces_instantiation() {
        let white_pieces = WhitePieces::new();
        assert_eq!(white_pieces.pieces.pawns.len(), 8);
        assert_eq!(
            &white_pieces.pieces.pawns[0].position_text,
            &String::from("a2")
        );
    }
}
