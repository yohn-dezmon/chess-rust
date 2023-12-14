pub trait Piece {
    // fn move(&self);

    fn points(&self) -> i32;
}

pub struct Pawn {
    points: i32;
}

pub struct Knight {
    points: i32;
}

pub struct Bishop {
    points: i32;
}

pub struct Rook {
    points: i32;
}

pub struct Queen {
    points: i32;
}

pub struct King {
    points: i32;
}



impl Piece for Pawn {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        // set default value to 1 for Pawn
        Pawn { points: 1 }
    }
}

impl Piece for Knight {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        Knight { points: 3 }
    }
}

impl Piece for Bishop {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        Bishop { points: 3 }
    }
}

impl Piece for Rook {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        // set default value to 1 for Pawn
        Rook { points: 5 }
    }
}

impl Piece for Queen {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        Queen { points: 9 }
    }
}

impl Piece for King {
    fn points(&self) -> i32 {
        self.points
    }

    fn new() -> Self {
        King { points: 0 }
    }
}
