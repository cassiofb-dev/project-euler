function evenFibonacciSum(limit) {
    let term_a = 0;
    let term_b = 1;
    let term_current = 1;

    let total = 0;
    while (term_current <= limit) {
        if (term_current % 2 == 0) {
            total += term_current;
        }

        term_current = term_a + term_b;
        term_b = term_a;
        term_a = term_current;
    }

    return total;
}

function main() {
    let result = evenFibonacciSum(4000000);

    console.log(result);
}

main();
