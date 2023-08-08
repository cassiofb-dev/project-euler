#include <math.h>
#include <stdio.h>

int isInteger(double number) {
    return floor(number) == number;
}

int specialPythagoreanTriplet(int triplet_sum) {
    for (int a = 1; a < triplet_sum; a++) {
        for (int b = a + 1; b < triplet_sum - a; b++) {
            double c = sqrt(a * a + b * b);

            if (isInteger(c) && a + b + c == triplet_sum) {
                return a * b * c;
            }
        }
    }

    return -1;
}

int main() {
    int result = specialPythagoreanTriplet(1000);

    printf("%d\n", result);

    return 0;
}
