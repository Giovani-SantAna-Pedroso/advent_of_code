use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    // println!("{:?}", args);
    let file_path = &args[1];
    println!("{}", file_path);
    let content = fs::read_to_string(file_path).expect("Should have been able to read the file");
    for line in content.lines() {
        println!("{}", line);
        let 
    }
    // println!("{:?}", content);
}
