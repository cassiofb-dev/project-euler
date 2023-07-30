function  sumAllMultiplesBellow(divisor, limit) {
    let total = 0;

    for (let i = 1; i < limit; i++) {
        if (i % divisor == 0) {
            total += i;
        }
    }

    return total;
}

function sumAll3And5MultiplesBellow(limit) {
    let total3 = sumAllMultiplesBellow(3, limit);
    let total5 = sumAllMultiplesBellow(5, limit);
    let total15 = sumAllMultiplesBellow(15, limit);

    return total3 + total5 - total15;
}

function main() {
    let result = sumAll3And5MultiplesBellow(1000);

    console.log(result);
}

main();
