function isNumberPalindrome(number) {
    let numberString = number.toString();
    let reverseNumberString = numberString.split("").reverse().join("");

    return numberString == reverseNumberString;
}

function largestPalindromeProduct(digits) {
    let lower_limit = 10 ** (digits - 1);
    let upper_limit = 10 ** digits;

    let highest = 0;
    let product;

    for (let i = lower_limit; i < upper_limit; i++) {
        for (let j = lower_limit; j < upper_limit; j++) {
            product = i * j;

            if (isNumberPalindrome(product) && product > highest) {
                highest = product;
            }
        }
    }

    return highest;
}

function main() {
    let result = largestPalindromeProduct(3);

    console.log(result);

    return 0;
}

main();
