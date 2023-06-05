use std::{str, fs};

const DATA_FILE: &str = "src/day3.txt";

fn main() {
    dbg!(fs::read_to_string(DATA_FILE).expect("File should've been read.").lines().map(|line| {
        let (left, right) = line.split_at(line.len() / 2);
        let item = left.chars().find(|i| right.contains(*i)).unwrap();
        match item {
            'a'..='z' => ((item as u8 - b'a') + 1) as u32,
            'A'..='Z' => ((item as u8 - b'A') + 1 + 26) as u32,
            _ => panic!("error")
        }
    }).sum::<u32>());

}
