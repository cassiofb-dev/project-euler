fn sum_square_difference(limit: usize) -> usize {
    let mut sum_of_squares: usize = 0;
    let mut square_of_sums: usize = 0;

    for i in 1..=limit {
        sum_of_squares += i * i;
        square_of_sums += i;
    }

    return square_of_sums * square_of_sums - sum_of_squares;
}

fn main() {
    let result: usize = sum_square_difference(100);

    println!("{}", result);
}
