use std::fs;

const DATA_FILE: &str = "src/day2.txt";
const W: u32 = 6; // Points when won
const D: u32 = 3; // Points when draw
const L: u32 = 0; // Points when lost
const ROCK: u32 = 1; // Rock points
const PAPER: u32 = 2; // Paper points
const SCISSORS: u32 = 3; // Scissors points

fn main() {
    let mut score: u32 = 0;
    let content = fs::read_to_string(DATA_FILE).expect("File should exist");
    content.split("\r\n").into_iter().for_each(|f| match f {
        "A X" => score += ROCK + D,
        "A Y" => score += PAPER + W,
        "A Z" => score += SCISSORS + L,
        "B X" => score += ROCK + L,
        "B Y" => score += PAPER + D,
        "B Z" => score += SCISSORS + W,
        "C X" => score += ROCK + W,
        "C Y" => score += PAPER + L,
        "C Z" => score += SCISSORS + D,
        _ => (),
    });

    println!("Part 1");
    dbg!(score);

    score = 0;
    content
        .split("\r\n")
        .into_iter()
        .for_each(|f: &str| match f {
            "A X" => score += SCISSORS + L,
            "A Y" => score += ROCK + D,
            "A Z" => score += PAPER + W,

            "B X" => score += ROCK + L,
            "B Y" => score += PAPER + D,
            "B Z" => score += SCISSORS + W,

            "C X" => score += PAPER + L,
            "C Y" => score += SCISSORS + D,
            "C Z" => score += ROCK + W,
            _ => (),
        });

        println!("Part 2");
        dbg!(score);
}

