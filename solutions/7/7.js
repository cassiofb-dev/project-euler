function nthPrime(position) {
    let max_size = 1000000;

    let is_prime = Array(max_size).fill(1);

    let i, j, prime_position = 0;
    for (i = 2; i < max_size; i++) {
        if (is_prime[i] == 1) {
            prime_position += 1;

            if (prime_position == position) {
                return i;
            }

            for (j = i * 2; j < max_size; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    return -1;
}

function main() {
    result = nthPrime(10001);

    console.log(result);
}

main();
