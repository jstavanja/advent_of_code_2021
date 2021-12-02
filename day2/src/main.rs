use std::fs;

fn main() {
    let input = fs::read_to_string("../../inputs/day2/1.txt").expect("Unable to read file");

    let instructions = input.lines();

    let mut depth = 0;
    let mut forward = 0;
    
    for ins in instructions {
        let direction_and_value = ins.split_whitespace().collect::<Vec<_>>();
        let direction = direction_and_value[0];
        let value = direction_and_value[1].parse::<i32>().unwrap();

        match direction {
            "forward" => {
                forward = forward + value;
            },
            "up" => {
                depth = depth - value;
            },
            "down" => {
                depth = depth + value;
            },
            _ => {
                panic!("Unknown action");
            }
        }
    }

    println!("{}", forward*depth);
}
