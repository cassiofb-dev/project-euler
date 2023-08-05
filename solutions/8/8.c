#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* getSeries() {
    char* file_contents = 0;

    long file_size;

    FILE *file = fopen("solutions/8/series.txt", "r");

    if (file) {
        fseek(file, 0, SEEK_END);

        file_size = ftell(file);

        fseek(file, 0, SEEK_SET);

        file_contents = malloc(file_size * sizeof(char));

        if (file_contents) {
            fread(file_contents, 1, file_size, file);
        }

        fclose(file);
    }

    if (file_contents) {
        return file_contents;
    } else {
        return 0;
    }
}

unsigned long long largestProductInSeries(int adjacents) {
    char* series = getSeries();

    if (series == 0) {
        return 0;
    }

    int series_length = strlen(series) - 2;

    unsigned long long largest_product = 1;
    unsigned long long current_product = 1;
    for (int i = 0; i < series_length - adjacents; i++) {
        for (int j = 0; j < adjacents; j++) {
            int number = series[i + j] - '0';
            current_product *= number;
        }

        if (current_product > largest_product) {
            largest_product = current_product;
        }

        current_product = 1;
    }

    free(series);

    return largest_product;
}

int main() {
    unsigned long long result = largestProductInSeries(13);

    printf("%llu\n", result);

    return 0;
}
