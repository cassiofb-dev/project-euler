fn largest_prime_factor(mut number: u64) -> u64 {
    let mut divisor: u64 = 2;

    loop {
        while number % divisor == 0 {
            number = number / divisor;
        }

        if number == 1 {
            break;
        }

        divisor += 1;
    }

    return divisor;
}

fn main() {
    let result: u64 = largest_prime_factor(600851475143);

    println!("{}", result);
}
