use std::fs;

// rustc main.rs && ./main

fn main() {
    // Read the file into a vector of strings
    let contents = fs::read_to_string("input.txt")
        .expect("Failed to read file");

    // Parse into (start, end) ranges just like test.py
    let data: Vec<(u64, u64)> = contents
        .trim()
        .split(',')
        .map(|line| {
            let mut parts = line.split('-');
            let start = parts.next().unwrap().parse::<u64>().unwrap();
            let end = parts.next().unwrap().parse::<u64>().unwrap();
            (start, end)
        })
        .collect();

    // Part 1
    let mut total = 0;

    for &(start, end) in &data {
      for i in start..=end {
        let s = i.to_string();
        let len = s.len();

        if len % 2 != 0 {
          continue;
        }

        let half = len / 2;
        let first_half: String = s.chars().take(half).collect(); 
        let second_half: String = s.chars().skip(half).collect();

        if first_half == second_half {
          total += i
        }
      }
    }

    println!("{total}");

    // Part 2
    let mut total = 0;

    for &(start, end) in &data {
      for i in start..=end {
        let s = i.to_string();
        let len = s.len();

        for chunk in 1..=(len / 2) {
          if len % chunk != 0 {
            continue;
          }

          let repeat_chunk: String = s.chars().take(chunk).collect();
          let repeated = repeat_chunk.repeat(len / chunk);
          if repeated == s && repeat_chunk != s {
            total += i;
            break
          }
        }
      }
    }

    println!("{total}")
}
