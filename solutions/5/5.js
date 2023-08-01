function leastCommonMultipleUntil(limit) {
    let lmc = 1;
    let divisor = 2;
    let numbers = Array(limit).fill(0).map((x, i) => i + 1);

    while (1) {

        while (numbers.filter(x => x % divisor == 0).length > 0) {
            numbers = numbers.map(x => x % divisor ? x : x / divisor);

            lmc *= divisor;
        }

        if (Math.max(...numbers) == 1) {
            break;
        }

        divisor += 1;
    }

    return lmc;
}

function main() {
    let result = leastCommonMultipleUntil(20);

    console.log(result);
}

main();
