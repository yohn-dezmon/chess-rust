#[derive(Debug)]
pub enum Color {
    Black,
    White,
}

struct Black {
    pub direction: i32,
}

struct White {
    pub direction: i32,
}

impl Black {
    pub fn new() -> Self {
        Black { direction: 1 }
    }
}

impl White {
    pub fn new() -> Self {
        // will be used in combination with `movement`
        // e.g. white pawns can only move up in the matrix
        White { direction: -1 }
    }
}
