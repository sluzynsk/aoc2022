// I got this code off Reddit. It's not mine - keeping here as an example
// of how to do this in Rust in case I find myself wanting to try it.

use std::fs;
use std::time::Instant;

fn main() {
    let now = Instant::now();
    let input = fs::read_to_string("./input").expect("Missing input file!");

    let get_round_result = |x: Vec<&str>| match x[..] {
        ["A", "X"] => 0 + 3,
        ["A", "Y"] => 3 + 1,
        ["A", "Z"] => 6 + 2,
        ["B", "X"] => 0 + 1,
        ["B", "Y"] => 3 + 2,
        ["B", "Z"] => 6 + 3,
        ["C", "X"] => 0 + 2,
        ["C", "Y"] => 3 + 3,
        ["C", "Z"] => 06 + 1,
        _ => {
            println!("Something went wrong");
            0
        }
    };

    let sum: u32 = input
        .lines()
        .map(|x| x.split(" ").collect())
        .map(|x| get_round_result(x))
        .sum();

    println!("{}", sum);
    println!("Execution time: {:?}", now.elapsed());
}
