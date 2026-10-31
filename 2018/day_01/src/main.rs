use std::collections::HashMap;

struct LineInfo {
    direction: i32, // if - -1; if + 1
    value: i32,
}

impl LineInfo {
    fn get_line_total(&self) -> i32 {
        self.value * self.direction
    }

    fn new(direction: i32, value: i32) -> LineInfo {
        LineInfo { direction, value }
    }
}

impl std::fmt::Display for LineInfo {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "value: {} => direction {}", self.value, self.direction)
    }
}

fn get_line_info(line: &str) -> LineInfo {
    if line == "\n" || line == "" {
        return LineInfo::new(0, 0);
    }

    let direction = if line.chars().nth(0).unwrap() == '-' {
        -1
    } else {
        1
    };
    let value = line[1..].parse::<i32>().unwrap();

    LineInfo::new(direction, value)
}

fn main() {
    let args: Vec<String> = std::env::args().collect();

    let file_name = &args[1];
    let file_content = std::fs::read_to_string(file_name).unwrap();
    let mut lines: Vec<_> = file_content.split('\n').collect();
    let mut ans1 = 0;

    // Ans1
    for line in &lines {
        let line_info = get_line_info(line);
        let line_total = line_info.get_line_total();
        ans1 += line_total;
    }
    println!("ans1: {:?}", ans1);

    // Ans2
    let mut tmp = 0;
    let mut ans2 = 0;
    let mut frequency_qtn: HashMap<i32, i8> = HashMap::new();
    let mut was_ans_2_found = false;

    loop {
        // println!("Loop");
        // println!("{:?}", &lines);
        for line in &lines {
            // print!("line: {}  {} ", tmp, line);
            if line == &"" {
                continue;
            }
            let line_info = get_line_info(line);
            let line_total = line_info.get_line_total();
            tmp += line_total;

            let qtn = frequency_qtn.entry(tmp).or_insert(0);
            *qtn += 1;

            if *qtn == 2 && !was_ans_2_found {
                // println!("was found {}", tmp);

                ans2 = tmp;
                was_ans_2_found = true;
                break;
            }

            // println!("tmp: {} => {:?}", tmp, frequency_qtn);
        }

        if was_ans_2_found {
            // println!("{:?}", frequency_qtn);
            break;
        }
    }

    println!("ans2: {:?}", ans2);
    // println!("has: {:?}", frequency_qtn);
}
