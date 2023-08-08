fn is_integer(number: f32) -> bool {
    return number.floor() == number;
}

fn special_pythagorean_triplet(triplet_sum: usize) -> usize {
    for a in 1..triplet_sum {
        for b in a+1..triplet_sum-a {
            let c: f32 = ((a * a + b * b) as f32).sqrt();

            if is_integer(c) && a + b + (c as usize) == triplet_sum {
                return a * b * (c as usize);
            }
        }
    }

    return 0;
}

fn main() {
    let result: usize = special_pythagorean_triplet(1000);

    println!("{}", result);
}