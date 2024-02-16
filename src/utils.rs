use std::fs::File;
use std::io::{self, prelude::*, BufReader};

pub fn parse_file(file: &str) -> Result<Vec<String>, io::Error> {
    let file = File::open(file)?;
    let reader = BufReader::new(file);
    reader.lines().collect()
}

pub fn parse_numbers(s: &str) -> Vec<i64> {
    s.split_whitespace()
        .filter_map(|num| num.parse::<i64>().ok())
        .collect()
}

pub fn extract_matrices(input: Vec<String>) -> Vec<Vec<Vec<i64>>> {
    let mut matrices: Vec<Vec<Vec<i64>>> = vec![];
    let mut current_matrix: Vec<Vec<i64>> = vec![];

    for line in input {
        let numbers = parse_numbers(&line);
        if !numbers.is_empty() {
            current_matrix.push(numbers);
        } else if !current_matrix.is_empty() {
            matrices.push(current_matrix);
            current_matrix = vec![];
        }
    }

    if !current_matrix.is_empty() {
        matrices.push(current_matrix);
    }

    matrices
}
