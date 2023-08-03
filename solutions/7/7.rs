fn nth_prime(position: usize) -> usize {
    const MAX_SIZE: usize = 1000000;

    let mut is_prime: [usize; MAX_SIZE] = [1; MAX_SIZE];

    let mut prime_position: usize = 0;
    for i in 2..MAX_SIZE {
        if is_prime[i] == 1 {
            prime_position += 1;

            if prime_position == position {
                return i;
            }

            for j in (i * 2..MAX_SIZE).step_by(i) {
                is_prime[j] = 0;
            }
        }
    }

    return 0;
}

fn main() {
    let result: usize = nth_prime(10001);

    println!("{}", result);
}
