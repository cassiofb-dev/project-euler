#include <stdio.h>
#include <stdbool.h>

int largestPrimeFactor(long int number) {
    int divisor = 2;

    while(true) {
        while(number % divisor == 0) {
            number = number / divisor;
        }

        if (number == 1) {
            break;
        }

        divisor += 1;
    }

    return divisor;
}

int main() {
    int result = largestPrimeFactor(600851475143);

    printf("%d", result);

    return 0;
}
