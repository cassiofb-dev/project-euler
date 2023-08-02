function sumSquareDifference(limit) {
    let sum_of_squares = 0;
    let square_of_sums = 0;

    for (let i = 1; i <= limit; i++) {
        sum_of_squares += i * i;
        square_of_sums += i;
    }

    return square_of_sums * square_of_sums - sum_of_squares;
}

function main() {
    let result = sumSquareDifference(100);

    console.log(result);

    return 0;
}

main();
