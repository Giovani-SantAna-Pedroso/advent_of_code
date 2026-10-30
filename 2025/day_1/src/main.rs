use std::env;
use std::fs;

struct Dial {
    position: i16,
    ans1: i16,
    ans2: i16,
}

impl Dial {
    const INIT_POS: i16 = 50;
    const START_POS: i16 = 0;
    const END_POS: i16 = 99;

    fn new() -> Self {
        Self {
            position: Self::INIT_POS,
            ans1: 0,
            ans2: 0,
        }
    }

    fn new_pos(&mut self, move_pos: &str) {
        let direction = if move_pos.chars().nth(0) == Some('R') {
            1
        } else {
            -1
        };

        let possitions: i16 = String::from(move_pos)[1..]
            .parse()
            .expect("Not a valid number");

        let moviment = direction * possitions;
        let mut new_pos = self.position + moviment;
        let mut alread_count = false;

        if new_pos < 0 {
            println!("{} => pass", move_pos);
            self.ans2 += 1;
            new_pos = Self::END_POS + 1 + new_pos % Self::END_POS;
            alread_count = true;
        } else if new_pos > 99 {
            println!("{} => pass", move_pos);
            self.ans2 += 1;
            new_pos = Self::START_POS - 1 + new_pos % Self::END_POS;
            alread_count = true;
        }

        if new_pos == 0 && !alread_count {
            println!("{} => pass", move_pos);
            self.ans1 += 1;
            self.ans2 += 1;
        }

        self.position = new_pos;

        // print!("{} -> ", move_pos);
        // println!("{} => {} ", moviment, new_pos);
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    // change to const latter
    let IS_DEBUG: bool = args.contains(&"-d".to_owned());
    let input_file = args[1].clone();

    let content = fs::read_to_string("./".to_owned() + &input_file).unwrap();
    let content_lines = content;

    let mut dial = Dial::new();
    for i in content_lines
        .lines()
        .take(content_lines.lines().count() - 1)
    {
        dial.new_pos(i);
    }
    println!("Ans1: {}", dial.ans1);
    println!("Ans2: {}", dial.ans2);
}
