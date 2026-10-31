use std::collections::HashSet;
use std::env;
use std::fs;

fn get_letters_times(line: &str) -> (i32, i32) {
    let mut letters: HashSet<char> = HashSet::new();
    let charts = line.chars();
    let mut times = (0, 0);

    for i in charts.clone() {
        letters.insert(i);
    }

    for i in letters {
        let count = charts.clone().filter(|&c| c == i).count();
        if count == 2 {
            times.0 = 1;
        } else if count == 3 {
            times.1 = 1;
        }
    }

    times
}

fn get_similar_lines(lines: Vec<&str>) -> (&str, &str) {
    let cp_lines = lines.clone();
    let amout_letters = lines[0].len();

    for i in lines {
        let i_chars: Vec<char> = i.chars().collect();

        for j in &cp_lines {
            let mut dif_chars = 0;
            let j_chars: Vec<char> = j.chars().collect();

            for x in 0..amout_letters {
                if i_chars[x] != j_chars[x] {
                    dif_chars += 1;
                }
            }
            if dif_chars == 1 {
                return (i, j);
            }
        }
    }
    ("", "")
}

fn get_ans2(words: (&str, &str)) {
    let chars_word_0: Vec<char> = words.0.chars().collect();
    let chars_word_1: Vec<char> = words.1.chars().collect();
    print!("Ans2: ");

    for i in 0..words.0.len() {
        if chars_word_0[i] == chars_word_1[i] {
            print!("{}", chars_word_0[i]);
        }
    }
    println!();
}

fn main() {
    let file_name = &env::args().collect::<Vec<String>>()[1];
    let file_content = fs::read_to_string(file_name).unwrap();
    let file_lines: Vec<&str> = file_content.lines().collect();
    let mut tmp_times: (i32, i32);

    //  1 = 2 letter
    //  2 = 3 letter
    let mut checksum: (i32, i32) = (0, 0);

    for line in &file_lines {
        tmp_times = get_letters_times(line);
        checksum.0 += tmp_times.0;
        checksum.1 += tmp_times.1;
    }

    println!("Ans1: {}", checksum.0 * checksum.1);

    let similar = get_similar_lines(file_lines);
    // println!("Similar lines: {:?}", similar);
    get_ans2(similar);
}
