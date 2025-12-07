use std::fs;

// rustc main.rs && ./main

fn main() {
    // Read the file into a vector of strings
    let contents = fs::read_to_string("input.txt")
        .expect("Failed to read file");

    // Or parse into (direction, number) tuples
    let parsed: Vec<(char, i32)> = contents
        .trim()
        .split('\n')
        .map(|line| {
            let direction = line.chars().next().unwrap();
            let number = line[1..].parse::<i32>().unwrap();
            (direction, number)
        })
        .collect();

    let mut hits: i32 = 0;
    let mut curr: i32 = 50;

    for (direction, amount) in parsed {
        let mut adjusted_amount: i32 = amount % 100;
        if direction == 'L' {
            adjusted_amount *= -1;
        }

        curr += adjusted_amount;

        if curr == 0 {
            hits += 1;
        } else if curr < 0 {
            curr = 100 + curr;
        } else if curr == 100 {
            curr = 0;
            hits += 1;
        } else if curr > 100 {
            curr -= 100;
        }
    }

    println!("Hits: {hits}");
}
