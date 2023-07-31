fn is_number_palindrome(number: u32) -> bool {
    let number_string: String = number.to_string();
    let reverse_number_string: String = number_string.chars().rev().collect();

    return number_string == reverse_number_string;
}

fn largest_palindrome_product(digits: u32) -> u32 {
    let lower_limit: u32 = 10u32.pow(digits - 1);
    let upper_limit: u32 = 10u32.pow(digits);

    let mut highest: u32 = 0;
    let mut product: u32;

    for i in lower_limit..=upper_limit {
        for j in lower_limit..=upper_limit {
            product = i * j;

            if is_number_palindrome(product) && product > highest {
                highest = product;
            }
        }
    }

    return highest;
}

fn main() {
    let result: u32 = largest_palindrome_product(3);

    println!("{}", result);
}
