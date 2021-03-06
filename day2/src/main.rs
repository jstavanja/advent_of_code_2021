use std::fs;

fn part1(input: &std::string::String) {
    calculate(input, false);
}

fn part2(input: &std::string::String) {
    calculate(input, true);
}

fn calculate(input: &std::string::String, use_aim: bool) {
    let instructions = input.lines();

    let mut depth = 0;
    let mut forward = 0;
    let mut aim = 0;
    
    for ins in instructions {
        let direction_and_value = ins.split_whitespace().collect::<Vec<_>>();
        let direction = direction_and_value[0];
        let value = direction_and_value[1].parse::<i32>().unwrap();

        match direction {
            "forward" => {
                forward = forward + value;
                if use_aim {
                    depth = depth + (aim * value);
                }
            },
            "up" => {
                if use_aim {
                    aim = aim - value;
                } else {
                    depth = depth - value;
                }
            },
            "down" => {
                if use_aim {
                    aim = aim + value;
                } else {
                    depth = depth + value;
                }
            },
            _ => {
                panic!("Unknown action");
            }
        }
    }

    println!("{}", forward*depth);
}

fn main() {
    let input = fs::read_to_string("../../inputs/day2/1.txt").expect("Unable to read file");
    part1(&input);
    part2(&input);
}
