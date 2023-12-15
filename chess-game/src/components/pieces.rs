pub trait Piece {
    // fn move(&self);

    fn get_points(&self) -> i32;
}

#[derive(Debug)]
pub struct Pawn {
    points: i32,
}

impl Piece for Pawn {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Pawn {
    pub fn new() -> Self {
        // set default value to 1 for Pawn
        Pawn { points: 1 }
    }
}

#[derive(Debug)]
pub struct Knight {
    points: i32,
}

impl Piece for Knight {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Knight {
    pub fn new() -> Self {
        Knight { points: 3 }
    }
}

#[derive(Debug)]
pub struct Bishop {
    points: i32,
}

impl Piece for Bishop {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Bishop {
    pub fn new() -> Self {
        Bishop { points: 3 }
    }
}

#[derive(Debug)]
pub struct Rook {
    points: i32,
}

impl Piece for Rook {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Rook {
    pub fn new() -> Self {
        Rook { points: 5 }
    }
}

#[derive(Debug)]
pub struct Queen {
    points: i32,
}

impl Piece for Queen {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl Queen {
    pub fn new() -> Self {
        Queen { points: 9 }
    }
}

#[derive(Debug)]
pub struct King {
    points: i32,
}

impl Piece for King {
    fn get_points(&self) -> i32 {
        self.points
    }
}

impl King {
    pub fn new() -> Self {
        King { points: 0 }
    }
}

// pub enum ChessPiece {
//     Pawn(Pawn),
//     Knight(Knight),
//     Bishop(Bishop),
//     Rook(Rook),
//     Queen(Queen),
//     King(King),
// }

pub struct ChessPieces {
    pawns: Vec<Pawn>,
    knights: Vec<Knight>,
    bishops: Vec<Bishop>,
    rooks: Vec<Rook>,
    queen: Vec<Queen>,
    king: Vec<King>,
}
