mod components;
use crate::components::pieces::{Bishop, King, Knight, Pawn, Piece, Queen, Rook};
// use crate::components::players::{Player1, Player2};

fn main() {
    let pawn = Pawn::new();
    println!("pawn's points: {}", pawn.get_points());
    let king = King::new();
    println!("king's points: {}", king.get_points());
    let bishop = Bishop::new();
    println!("bishop's points: {}", bishop.get_points());
    let rook = Rook::new();
    println!("rook's points: {}", rook.get_points());
    let queen = Queen::new();
    println!("queen's points: {}", queen.get_points());
    let knight = Knight::new();
    println!("knight's points: {}", knight.get_points());
}
