#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int isNumberPalindrome(int number) {
    int size = snprintf(NULL, 0, "%d", number);

    char *buffer = malloc(size + 1);

    snprintf(buffer, size + 1, "%d", number);

    for (int i = 0; i < size / 2; i++) {
        if (buffer[i] != buffer[size - i - 1]) {
            free(buffer);
            return false;
        }
    }

    free(buffer);
    return true;
}

int largestPalindromeProduct(int digits) {
    int lower_limit = pow(10, digits - 1);
    int upper_limit = pow(10, digits);

    int highest = 0;
    int product;

    for (int i = lower_limit; i < upper_limit; i++) {
        for (int j = lower_limit; j < upper_limit; j++) {
            product = i * j;

            if (isNumberPalindrome(product) && product > highest) {
                highest = product;
            }
        }
    }

    return highest;
}

int main() {
    int result = largestPalindromeProduct(3);

    printf("%d", result);

    return 0;
}
