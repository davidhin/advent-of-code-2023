extern crate regex;
use std::collections::HashMap;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("data/day4b.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    let lines: Vec<String> = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();

    let mut card_copies: HashMap<i32, i32> = HashMap::new();

    for line in lines {
        if let [card_num, card_str] = line.split(':').collect::<Vec<&str>>().as_slice() {
            let card_num: i32 = card_num
                .split_whitespace()
                .last()
                .unwrap()
                .parse::<i32>()
                .unwrap();

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

                for card_idx in (card_num + 1)..(card_num + intersection.len() as i32 + 1) {
                    *card_copies.entry(card_idx).or_insert(1) +=
                        *card_copies.entry(card_num).or_insert(1);
                }
                card_copies.entry(card_num).or_insert(1);
            }
        }
    }

    total = card_copies.values().sum();
    println!("Total: {:?}", total);
    Ok(())
}
