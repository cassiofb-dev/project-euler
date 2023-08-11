#include <stdio.h>
#include <stdlib.h>

void fillArray(int* is_prime, int size, int value) {
    for (int i = 0; i < size; i++) {
        is_prime[i] = value;
    }
}

unsigned long long sumPrimesUntil(int limit) {
    int max_size = limit;

    int* is_prime = malloc(max_size * sizeof(int));

    fillArray(is_prime, max_size, 1);

    unsigned long long prime_sum = 0;
    for (int i = 2; i < max_size; i++) {
        if (is_prime[i] == 1) {
            prime_sum += i;

            for (int j = i * 2; j < max_size; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    free(is_prime);
    return prime_sum;
}

int main() {
    unsigned long long result = sumPrimesUntil(2000000);

    printf("%llu\n", result);

    return 0;
}
