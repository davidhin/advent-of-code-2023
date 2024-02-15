extern crate regex;
use regex::Regex;
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

#[derive(Debug)]
struct Schematic {
    lines: Vec<String>,
}

impl Schematic {
    fn adj_to_special(&self, row: usize, col: usize) -> bool {
        [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        .iter()
        .any(|&(dr, dc)| {
            let (adj_row, adj_col) = (row as isize + dr, col as isize + dc);
            if adj_row >= 0 && adj_col >= 0 {
                let (adj_row, adj_col) = (adj_row as usize, adj_col as usize);
                self.lines
                    .get(adj_row)
                    .and_then(|line| line.chars().nth(adj_col))
                    .map_or(false, |ch| ch != '.' && !ch.is_digit(10))
            } else {
                false
            }
        })
    }

    fn line_parts(&self, row: usize) -> i32 {
        let re = Regex::new(r"\d+").unwrap();
        let mut total = 0;
        for mat in re.find_iter(self.lines.get(row).unwrap()) {
            let any_adj_special = (mat.start()..mat.end()).any(|x| self.adj_to_special(row, x));
            if any_adj_special {
                total += mat.as_str().parse::<i32>().unwrap_or(0);
            }
        }
        total
    }
}

fn main() -> io::Result<()> {
    let file = File::open("data/day3a.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    let lines: Vec<String> = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();

    let schematic: Schematic = Schematic { lines };

    for i in 0..schematic.lines.len() {
        total += schematic.line_parts(i);
    }

    println!("{}", total);
    Ok(())
}
