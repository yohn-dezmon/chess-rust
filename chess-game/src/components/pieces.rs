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
    position_text: String,
}

pub struct ChessPieces {
    pawns: Vec<ChessPiece>,
    knights: Vec<ChessPiece>,
    bishops: Vec<ChessPiece>,
    rooks: Vec<ChessPiece>,
    queen: Vec<ChessPiece>,
    king: Vec<ChessPiece>,
}

impl ChessPieces {
    pub fn new() -> Self {
        ChessPieces {
            pawns: Vec::new(),
            knights: Vec::new(),
            bishops: Vec::new(),
            rooks: Vec::new(),
            queen: Vec::new(),
            king: Vec::new(),
        }
    }
}

pub struct BlackPieces {
    pieces: ChessPieces,
}

const LETTERS: Vec<char> = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g'];

// the implementation of ChessPieces for the black pieces
impl BlackPieces {
    pub fn new() -> Self {
        let mut pawns = Vec::new();
        const COLOR: Color = Color::Black;
        for letter in LETTERS {
            for col in 0..8 {
                let piece = ChessPiece {
                    piece_type: PieceType::Pawn,
                    color: COLOR,
                    position_xy: vec![1, col],
                    position_text: format!("{}7", letter),
                };
                pawns.push(piece);
            }
        }
        BlackPieces {
            pieces: ChessPieces { pawns: pawns },
        }
    }
}

// impl ChessPiece {
//     pub fn new() -> Self {
//         ChessPiece {
//             piece_type: PieceType::Pawn,
//             color: Color::Black,
//             position_xy: vec![],
//             position_text: String::new(),
//         }
//     }
// }

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
