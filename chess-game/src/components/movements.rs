pub struct Directions {
    unbounded: bool,
    unit_direction: Vec<i32>
}

pub struct WhitePawnMovements {
    up: Directions,
    up_right: Directions,
    up_left: Directions,
}

impl WhitePawnMovements {
    pub fn new() -> Self {
        WhitePawnMovements {
            up: Directions { unbounded: false, unit_direction: vec![-1, 0] },
            up_right: Directions { unbounded: false, unit_direction: vec![-1, 1] },
            up_left: Directions { unbounded: false, unit_direction: vec![-1, -1] },
        }
    }
}
