use crate::components::pieces::ChessPieces;
use crate::components::color::Color;

pub struct Player1 {
    // when to use String vs. &str
    user_name: String,
    total_points: i32,
    point_balance: i32,
    team: Color,
    pieces: ChessPieces,
}


impl Player1 {
    pub fn new() -> Self {
        Player1 {
            user_name: String::new(),
            total_points: 39,
            point_balance: 0,
            team: Color::White,
            pieces: ChessPieces::new(),
        }
    }
}

struct Player2 {
    user_name: String,
    total_points: i32,
    point_balance: i32,
    team: Color,
}

impl Player2 {
    fn new() -> Self {
        total_points = 39;
    }
}
