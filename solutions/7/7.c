#include <stdio.h>
#include <stdlib.h>

void fillArray(int* is_prime, int size, int value) {
    for (int i = 0; i < size; i++) {
        is_prime[i] = value;
    }
}

int nthPrime(int position) {
    int max_size = 1000000;

    int* is_prime = malloc(max_size * sizeof(int));

    fillArray(is_prime, max_size, 1);

    int i, j, prime_position = 0;
    for (i = 2; i < max_size; i++) {
        if (is_prime[i] == 1) {
            prime_position += 1;

            if (prime_position == position) {
                free(is_prime);
                return i;
            }

            for (j = i * 2; j < max_size; j += i) {
                is_prime[j] = 0;
            }
        }
    }

    free(is_prime);
    return -1;
}

int main() {
    int result = nthPrime(10001);

    printf("%d", result);

    return 0;
}
