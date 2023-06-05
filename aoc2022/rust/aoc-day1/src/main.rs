use std::fs;
const SINGLE_LBR: &str = "\r\n";
const DOUBLE_LBR: &str = "\r\n\r\n";
const FILE_PATH: &str = "src/day1.txt";

fn main() {
    let contents: String = fs::read_to_string(FILE_PATH).expect("File should exist...");
    let mut elves: Vec<i32> = contents.split(DOUBLE_LBR).map(|elf| {
        elf.split(SINGLE_LBR)
            .filter_map(|l| l.trim().parse::<i32>().ok())
            .sum::<i32>()
    }).collect();
    
    elves.sort_by(| a, b | b.cmp(a));

    println!("Part 1");
    dbg!(elves[0]);

    println!("Part 2");
    dbg!(elves.iter().take(3).sum::<i32>());
}
