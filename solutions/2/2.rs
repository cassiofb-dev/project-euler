fn even_fibonacci_sum(limit: u32) -> u32 {
    let mut term_a: u32 = 0;
    let mut term_b: u32 = 1;
    let mut term_current: u32 = 1;

    let mut total: u32 = 0;
    while term_current <= limit {
        if term_current % 2 == 0 {
            total += term_current;
        }

        term_current = term_a + term_b;
        term_b = term_a;
        term_a = term_current;
    }

    return total;
}

fn main() {
    let result: u32 = even_fibonacci_sum(4000000);

    println!("{}", result);
}
