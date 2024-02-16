extern crate regex;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("data/day4a.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    let lines: Vec<String> = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();

    for line in lines {
        if let Some(card_str) = line.split(':').last() {
            if let [first_part, second_part] = card_str.split('|').collect::<Vec<&str>>().as_slice()
            {
                let winning: Vec<i32> = first_part
                    .split_whitespace()
                    .map(|s| s.parse::<i32>().unwrap())
                    .collect();
                let current: Vec<i32> = second_part
                    .split_whitespace()
                    .map(|s| s.parse::<i32>().unwrap())
                    .collect();

                let intersection: Vec<i32> = current
                    .iter()
                    .filter(|&x| winning.contains(x))
                    .cloned()
                    .collect();

                if intersection.len() > 0 {
                    total += 2_i32.pow((intersection.len() - 1) as u32)
                }
            }
        }
    }

    println!("Total: {:?}", total);
    Ok(())
}
