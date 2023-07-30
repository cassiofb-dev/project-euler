def largestPrimeFactor(number):
    divisor = 2

    while True:
        while number % divisor == 0:
            number = number / divisor

        if number == 1:
            break

        divisor += 1

    return divisor

def main():
    result = largestPrimeFactor(600851475143)

    print(result)

if __name__ == '__main__':
    main()
