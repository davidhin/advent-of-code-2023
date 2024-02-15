use std::collections::HashMap;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::ops::Add;

#[derive(Debug)]
struct DieSet {
    red: i32,
    green: i32,
    blue: i32,
}

impl DieSet {
    fn from_die_set_str(s: &str) -> Self {
        let die_nums: Vec<&str> = s.trim().split(',').map(|s| s.trim()).collect();
        let mut colours: HashMap<String, i32> = HashMap::new();
        die_nums.iter().for_each(|&item| {
            let die_num_data: Vec<&str> = item.split_whitespace().collect();
            let die_num: i32 = die_num_data.first().unwrap().parse::<i32>().unwrap();
            let die_colour: String = die_num_data.last().unwrap().to_string();
            *colours.entry(die_colour).or_insert(0) += die_num;
        });

        DieSet {
            red: *colours.get("red").unwrap_or(&0),
            green: *colours.get("green").unwrap_or(&0),
            blue: *colours.get("blue").unwrap_or(&0),
        }
    }
}

impl Add for DieSet {
    type Output = DieSet;

    fn add(self, other: DieSet) -> DieSet {
        DieSet {
            red: self.red + other.red,
            green: self.green + other.green,
            blue: self.blue + other.blue,
        }
    }
}

fn parse_game(game_str: &str) -> Vec<DieSet> {
    game_str
        .split(':')
        .last()
        .unwrap()
        .split(';')
        .map(DieSet::from_die_set_str)
        .collect()
}

fn valid_game(game_str: &str) -> i32 {
    let have: DieSet = DieSet {
        red: 12,
        green: 13,
        blue: 14,
    };
    for required in parse_game(game_str) {
        if required.red > have.red || required.blue > have.blue || required.green > have.green {
            return 0;
        }
    }

    game_str
        .split(':')
        .next()
        .unwrap()
        .split_whitespace()
        .last()
        .unwrap()
        .parse::<i32>()
        .unwrap()
}

fn main() -> io::Result<()> {
    let file = File::open("data/day2a.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    for line in reader.lines() {
        total += valid_game(&line?);
    }

    println!("{}", total);
    Ok(())
}
