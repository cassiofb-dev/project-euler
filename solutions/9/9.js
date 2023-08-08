function specialPythagoreanTriplet(triplet_sum) {
    for (let a = 1; a < triplet_sum; a++) {
        for (let b = a + 1; b < triplet_sum - a; b++) {
            const c = Math.sqrt(a * a + b * b);

            if (Number.isInteger(c) && a + b + c === triplet_sum) {
                return a * b * c;
            }
        }
    }

    return -1;
}

function main() {
    const result = specialPythagoreanTriplet(1000);

    console.log(result);
}

main();
