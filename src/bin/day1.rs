extern crate regex;
use regex::Regex;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn numbers_in_string(s: &str) -> Vec<&str> {
    let re = Regex::new(r"\d").unwrap();
    re.find_iter(s).map(|mat| mat.as_str()).collect()
}

fn calibration_value(input_str: &str) -> String {
    let numbers: Vec<&str> = numbers_in_string(input_str);
    format!("{}{}", numbers.first().unwrap(), numbers.last().unwrap())
}

fn main() -> io::Result<()> {
    let file = File::open("data/day1.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    for line in reader.lines() {
        total += calibration_value(&line?).parse::<i32>().unwrap();
    }

    println!("{}", total);
    Ok(())
}
