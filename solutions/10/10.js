function sumPrimesUntil(limit) {
    let is_prime = Array(limit).fill(1);

    let prime_sum = 0;
    for (let i = 2; i < limit; i++) {
        if (is_prime[i] == 1) {
            prime_sum += i;

            for (let j = i * 2; j < limit; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    return prime_sum;
}

function main() {
    result = sumPrimesUntil(2000000);

    console.log(result);
}

main();
