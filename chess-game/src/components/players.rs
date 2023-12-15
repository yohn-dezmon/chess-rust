use crate::components::pieces::ChessPieces;
use crate::components::teams::Team;

pub struct Player1 {
    // when to use String vs. &str
    user_name: String,
    total_points: i32,
    point_balance: i32,
    team: Team,
    pieces: ChessPieces,
}


impl Player1 {
    pub fn new() -> Self {
        Player1 {
            user_name: String::new(),
            total_points: 39,
            point_balance: 0,
            team: Team::White
            pieces: 
        }
    }
}

struct Player2 {
    user_name: String,
    total_points: i32,
    point_balance: i32,
    team: Team,
}

impl Player2 {
    fn new() -> Self {
        total_points = 39;
    }
}
