extern crate regex;
use regex::Match;
use regex::Regex;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

#[derive(Debug)]
struct NumberMatch {
    position: i32,
    number: i32,
}

impl NumberMatch {
    fn from_match(m: Match) -> Self {
        let position = m.start() as i32; // Adding 1 to make the position 1-based
        let number = match m.as_str() {
            "one" => 1,
            "two" => 2,
            "three" => 3,
            "four" => 4,
            "five" => 5,
            "six" => 6,
            "seven" => 7,
            "eight" => 8,
            "nine" => 9,
            _ => m.as_str().parse().unwrap_or(0), // Attempt to parse as integer
        };

        NumberMatch { position, number }
    }
}

fn get_number_matches(s: &str, regex_str: &str) -> Vec<NumberMatch> {
    let re = Regex::new(regex_str).unwrap();
    re.find_iter(s)
        .map(|mat| NumberMatch::from_match(mat))
        .collect()
}

fn numbers_in_string(s: &str) -> Vec<NumberMatch> {
    let patterns = vec![
        r"\d", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
    ];

    let mut all_matches: Vec<NumberMatch> = Vec::new();

    for pattern in patterns {
        all_matches.extend(get_number_matches(s, pattern));
    }

    all_matches.sort_by_key(|x| x.position);
    all_matches
}

fn calibration_value(input_str: &str) -> String {
    let number_matches: Vec<NumberMatch> = numbers_in_string(input_str);
    let first_number = number_matches.first().map_or(0, |x| x.number);
    let last_number = number_matches.last().map_or(0, |x| x.number);
    format!("{}{}", first_number, last_number)
}

fn main() -> io::Result<()> {
    let file = File::open("data/day1b.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    for line in reader.lines() {
        total += calibration_value(&line?).parse::<i32>().unwrap();
    }

    println!("{}", total);
    Ok(())
}
