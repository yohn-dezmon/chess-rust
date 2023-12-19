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

const LETTERS: Vec<char> = vec!['a', 'b', 'c', 'd', 'e', 'f', 'g'];

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

        let mut knights = Vec::new();
        let knight_left = ChessPiece {
            piece_type: PieceType::Knight,
            color: COLOR,
            position_xy: vec![0, 1],
            position_text: String::from("b8"),
        };
        let knight_right = ChessPiece {
            piece_type: PieceType::Knight,
            color: COLOR,
            position_xy: vec![0, 6],
            position_text: String::from("g8"),
        };
        knights.push(knight_left);
        knights.push(knight_right);

        let mut bishops = Vec::new();
        let bishop_left = ChessPiece {
            piece_type: PieceType::Bishop,
            color: COLOR,
            position_xy: vec![0, 2],
            position_text: String::from("c8"),
        };
        let bishop_right = ChessPiece {
            piece_type: PieceType::Bishop,
            color: COLOR,
            position_xy: vec![0, 5],
            position_text: String::from("f8"),
        };
        bishops.push(bishop_left);
        bishops.push(bishop_right);

        let mut rooks = Vec::new();
        let rook_left = ChessPiece {
            piece_type: PieceType::Bishop,
            color: COLOR,
            position_xy: vec![0, 0],
            position_text: String::from("a8"),
        };
        let rook_right = ChessPiece {
            piece_type: PieceType::Bishop,
            color: COLOR,
            position_xy: vec![0, 7],
            position_text: String::from("h8"),
        };
        bishops.push(rook_left);
        bishops.push(rook_right);

        let mut queen = vec![ChessPiece {
            piece_type: PieceType::Queen,
            color: COLOR,
            position_xy: vec![0, 3],
            position_text: String::from("d8"),
        }];

        let mut king = vec![ChessPiece {
            piece_type: PieceType::King,
            color: COLOR,
            position_xy: vec![0, 4],
            position_text: String::from("e8"),
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
