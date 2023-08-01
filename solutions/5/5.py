def leastCommonMultipleUntil(limit):
    lmc = 1
    divisor = 2
    numbers = list(range(1, limit + 1))

    while True:
        while any(number % divisor == 0 for number in numbers):
            numbers = [number if number % divisor else number / divisor for number in numbers]
            lmc *= divisor
        if max(numbers) == 1:
            break
        divisor += 1
    return lmc

def main():
    result = leastCommonMultipleUntil(20)
    print(result)

if __name__ == "__main__":
    main()
