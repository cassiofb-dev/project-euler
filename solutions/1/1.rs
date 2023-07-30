fn sum_all_multiples_bellow(divisor: u32, limit: u32) -> u32 {
    let mut total: u32 = 0;

    for i in 1..=limit - 1 {
        if i % divisor == 0 {
            total += i;
        }
    }

    return total;
}

fn sum_all_3_and_5_multiples_bellow(limit: u32) -> u32 {
    let total3: u32 = sum_all_multiples_bellow(3, limit);
    let total5: u32 = sum_all_multiples_bellow(5, limit);
    let total15: u32 = sum_all_multiples_bellow(15, limit);

    return total3 + total5 - total15;
}

fn main() {
    let result: u32 = sum_all_3_and_5_multiples_bellow(1000);

    println!("{}", result);
}
