extern crate regex;
use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, prelude::*, BufReader};

#[derive(Debug)]
struct Schematic {
    lines: Vec<String>,
    mapped: Vec<Vec<String>>,
    keys: HashMap<String, i32>,
}

impl Schematic {
    fn parse(lines: Vec<String>) -> Schematic {
        let mut keys: HashMap<String, i32> = HashMap::new();
        let mut mapped: Vec<Vec<String>> = lines
            .clone()
            .into_iter()
            .map(|line| line.chars().map(|c| c.to_string()).collect())
            .collect();
        let re = Regex::new(r"\d+").unwrap();

        let mut num_key = 0;
        for row_idx in 0..mapped.len() {
            for mat in re.find_iter(lines.get(row_idx).unwrap()) {
                for map_idx in mat.start()..mat.end() {
                    mapped[row_idx][map_idx] = num_key.to_string();
                }
                keys.insert(num_key.to_string(), mat.as_str().parse::<i32>().unwrap());
                num_key += 1;
            }
        }

        Schematic {
            lines,
            mapped,
            keys,
        }
    }

    fn adj_numbers(&self, row: usize, col: usize) -> i32 {
        let current = self.mapped.get(row).unwrap().get(col).unwrap();
        if current != "*" {
            return 0;
        }
        let mut adj_nums: HashSet<String> = HashSet::new(); // Create a set to store your unique entries
        let mut product = 1;

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
        .for_each(|&(dr, dc)| {
            let (adj_row, adj_col) = (
                isize::try_from(row).unwrap_or_default() + dr,
                isize::try_from(col).unwrap_or_default() + dc,
            );

            if adj_row >= 0 && adj_col >= 0 {
                // Convert back to usize safely after checking they are positive
                let (adj_row, adj_col) = (adj_row as usize, adj_col as usize);

                // Perform lookup once, handling potential None cases gracefully
                if let Some(row_vec) = self.mapped.get(adj_row) {
                    if let Some(value) = row_vec.get(adj_col) {
                        // Now, check the key and perform action only once
                        if self.keys.contains_key(value) {
                            // Perform your intended action with 'entry'
                            adj_nums.insert(value.clone());
                        }
                    }
                }
            }
        });

        if adj_nums.len() == 2 {
            for num in adj_nums.iter() {
                product *= self.keys.get(num).unwrap();
            }
            return product;
        } else {
            0
        }
    }
}

fn main() -> io::Result<()> {
    let file = File::open("data/day3b.txt")?;
    let reader = BufReader::new(file);
    let mut total: i32 = 0;

    let lines: Vec<String> = reader
        .lines()
        .collect::<Result<Vec<String>, io::Error>>()
        .unwrap();

    let schematic: Schematic = Schematic::parse(lines);

    for (x, line) in schematic.lines.iter().enumerate() {
        for (y, ch) in line.chars().enumerate() {
            if ch == '*' {
                total += schematic.adj_numbers(x, y);
            }
        }
    }

    println!("{}", total);
    Ok(())
}
