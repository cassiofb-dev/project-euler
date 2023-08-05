use std::fs;
use std::convert::TryFrom;

fn get_series() -> String {
    let file_contents = fs::read_to_string("solutions/8/series.txt").expect("Unable to read file");

    return file_contents;
}

fn largest_product_in_series(adjacents: usize) -> usize {
    let series: String = get_series();

    let mut largest_product: usize = 1;
    let mut current_product: usize = 1;
    for i in 0..series.chars().count() - adjacents {
        for j in 0..adjacents {
            let number: u32 = series.chars().nth(i + j).unwrap().to_digit(10).unwrap();
            current_product *= usize::try_from(number).unwrap();
        }

        if current_product > largest_product {
            largest_product = current_product;
        }

        current_product = 1;
    }

    return largest_product;
}

fn main() {
    let result: usize = largest_product_in_series(13);

    println!("{}", result);
}
