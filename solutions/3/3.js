function largestPrimeFactor(number) {
    let divisor = 2;

    while (true) {
        while (number % divisor == 0) {
            number = number / divisor;
        }

        if (number == 1) {
            break;
        }

        divisor += 1;
    }

    return divisor;
}

function main() {
    let result = largestPrimeFactor(600851475143);

    console.log(result);
}

main();
