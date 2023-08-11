fn sum_primes_until(limit: usize) -> usize {
    let mut is_prime = vec![1; limit];

    let mut prime_sum: usize = 0;
    for i in 2..limit {
        if is_prime[i] == 1 {
            prime_sum += i;

            for j in (i * 2..limit).step_by(i) {
                is_prime[j] = 0;
            }
        }
    }

    return prime_sum;
}

fn main() {
    let result: usize = sum_primes_until(2000000);

    println!("{}", result);
}
