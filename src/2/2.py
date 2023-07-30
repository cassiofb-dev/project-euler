def evenFibonacciSum(limit):
    term_a = 0
    term_b = 1
    term_current = 1

    total = 0
    while term_current <= limit:
        if (term_current % 2 == 0):
            total += term_current

        term_current = term_a + term_b
        term_b = term_a
        term_a = term_current

    return total

def main():
    result = evenFibonacciSum(4000000)

    print(result)

if __name__ == '__main__':
    main()
