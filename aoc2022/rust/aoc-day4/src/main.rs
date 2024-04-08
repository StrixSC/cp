use std::{str, fs};

const DATA_FILE: &str = "src/day4.txt";

fn main() {
    let input_data = fs::read_to_string(DATA_FILE).expect("Could not read from file or file doesn't exist.")
    .lines()
    .map(|l| {
        let splitted = l.split(",").map(|i| {
            i.split('-')
        });
    });
}
