#include <stdio.h>

int evenFibonacciSum(int limit) {
    int term_a = 0;
    int term_b = 1;
    int term_current = 1;

    int total = 0;
    while(term_current <= limit) {
        if (term_current % 2 == 0) {
            total += term_current;
        }

        term_current = term_a + term_b;
        term_b = term_a;
        term_a = term_current;
    }

    return total;
}

int main() {
    int result = evenFibonacciSum(4000000);

    printf("%d", result);

    return 0;
}
