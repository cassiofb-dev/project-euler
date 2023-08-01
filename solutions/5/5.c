#include <stdio.h>

int initializeArray(int* numbers_buffer, int limit) {
    for (int i = 0; i < limit; i++) {
        numbers_buffer[i] = i + 1;
    }
}

int maximumValue(int* numbers_buffer, int limit) {
    int max_index = 0;

    for (int i = 0; i < limit; i++) {
        if (numbers_buffer[i] > numbers_buffer[max_index]) {
            max_index = i;
        }
    }

    return numbers_buffer[max_index];
}

int anyDivisibleBy(int* numbers_buffer, int limit, int divisor) {
    for (int i = 0; i < limit; i++) {
        if (numbers_buffer[i] % divisor == 0) {
            return 1;
        }
    }

    return 0;
}

void divideArray(int* numbers_buffer, int limit, int divisor) {
    for (int i = 0; i < limit; i++) {
        if (numbers_buffer[i] % divisor == 0) {
            numbers_buffer[i] /= divisor;
        }
    }
}

int leastCommonMultipleUntil(int limit) {
    int lmc = 1;
    int divisor = 2;
    int numbers_buffer[100];

    initializeArray(numbers_buffer, limit);

    while (1) {
        while (anyDivisibleBy(numbers_buffer, limit, divisor)) {
            divideArray(numbers_buffer, limit, divisor);
            lmc *= divisor;
        }

        if (maximumValue(numbers_buffer, limit) == 1) {
            break;
        }

        divisor += 1;
    }

    return lmc;
}

int main() {
    int result = leastCommonMultipleUntil(20);

    printf("%d", result);

    return 0;
}
