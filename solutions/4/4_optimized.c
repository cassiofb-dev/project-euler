#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

static char buffer[256];

static int bchop(int n) {
    int r = 1;

    if (n >= 100000000) {
        r += 8;
        n /= 100000000;
    }

    if (n >= 10000) {
        r += 4;
        n /= 10000;
    }

    if (n >= 100) {
        r += 2;
        n /= 100;
    }

    if (n >= 10) {
        r++;
    }

    return r;
}

static inline int isNumberPalindrome(int number) {
    if (number < 1) {
        return false;
    }

    int size = bchop(number);

    for (int i = 0; number; ++i, number /= 10) {
      buffer[i] = '0' + (number % 10);
    }

    for (int i = 0, j = size / 2; i < j; ++i) {
        if (buffer[i] != buffer[size - i - 1]) {
            return false;
        }
    }

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

// thanks to ogromnyvova
