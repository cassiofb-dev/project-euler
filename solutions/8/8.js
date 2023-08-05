function getSeries() {
    let fs = require("fs");

    let file = fs.readFileSync("solutions/8/series.txt");

    let file_contents = file.toString("utf-8");

    return file_contents;
}

function largestProductInSeries(adjacents) {
    let series = getSeries();

    let largest_product = 1;
    let current_product = 1;
    for (let i = 0; i < series.length - adjacents; i++) {
        for (let j = 0; j < adjacents; j++) {
            let number = Number(series[i + j]);
            current_product *= number;
        }

        if (current_product > largest_product) {
            largest_product = current_product;
        }

        current_product = 1;
    }

    return largest_product;
}

function main() {
    let result = largestProductInSeries(13);

    console.log(result);
}

main();
