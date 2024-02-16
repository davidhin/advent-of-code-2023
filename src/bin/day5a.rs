use advent_of_code_2023::utils;

fn dest_from_matrix_map(i: i64, mat: Vec<Vec<i64>>) -> i64 {
    for row in mat.iter() {
        if let [dest, source, range] = row.as_slice() {
            if i >= *source && i < (*source + *range) {
                return dest + (i - source);
            }
        }
    }

    i
}

fn seed_to_location(seed: i64, maps: Vec<Vec<Vec<i64>>>) -> i64 {
    let mut curr: i64 = seed;
    for map in maps {
        curr = dest_from_matrix_map(curr, map);
    }
    curr
}

fn main() {
    let data: Vec<Vec<Vec<i64>>> =
        utils::extract_matrices(utils::parse_file("data/day5a.txt").unwrap());

    let seeds: Vec<i64> = data
        .get(0)
        .and_then(|matrix| matrix.get(0))
        .cloned()
        .unwrap_or_else(Vec::new);

    // Transform each seed using `seed_to_location`, then find the minimum value
    let transformed_seeds: Vec<i64> = seeds
        .iter()
        .map(|&seed| seed_to_location(seed, data[1..].to_vec()))
        .collect();

    let min_seed = transformed_seeds.iter().min();

    println!("{:?}", min_seed.unwrap())
}
