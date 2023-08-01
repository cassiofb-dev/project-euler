fn initialize_array(numbers_buffer: &mut [usize], limit: usize) {
    for i in 0..=limit - 1 {
        numbers_buffer[i] = i + 1;
    }
}

fn maximum_value(numbers_buffer: &mut [usize], limit: usize) -> usize {
    let mut max_index: usize = 0;

    for i in 0..=limit - 1 {
        if numbers_buffer[i] > numbers_buffer[max_index] {
            max_index = i;
        }
    }

    return numbers_buffer[max_index];
}

fn any_divisible_by(numbers_buffer: &mut [usize], limit: usize, divisor: usize) -> bool {
    for i in 0..=limit - 1 {
        if numbers_buffer[i] % divisor == 0 {
            return true;
        }
    }

    return false;
}

fn divide_array(numbers_buffer: &mut [usize], limit: usize, divisor: usize) {
    for i in 0..=limit - 1 {
        if numbers_buffer[i] % divisor == 0 {
            numbers_buffer[i] /= divisor;
        }
    }
}

fn least_common_multiple_until(limit: usize) -> usize {
    let mut lmc: usize = 1;
    let mut divisor: usize = 2;
    let mut numbers_buffer: [usize; 100] = [0; 100];

    initialize_array(&mut numbers_buffer, limit);

    loop {
        while any_divisible_by(&mut numbers_buffer, limit, divisor) {
            divide_array(&mut numbers_buffer, limit, divisor);
            lmc *= divisor;
        }

        if maximum_value(&mut numbers_buffer, limit) == 1 {
            break;
        }

        divisor += 1;
    }

    return lmc;
}

fn main() {
    let result: usize = least_common_multiple_until(20);

    println!("{}", result);
}
