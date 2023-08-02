#include <stdio.h>

int sumSquareDifference(int limit) {
    int sum_of_squares = 0;
    int square_of_sums = 0;

    for (int i = 1; i <= limit; i++) {
        sum_of_squares += i * i;
        square_of_sums += i;
    }

    return square_of_sums * square_of_sums - sum_of_squares;
}

int main() {
    int result = sumSquareDifference(100);

    printf("%d", result);

    return 0;
}
