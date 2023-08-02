def sumSquareDifference(limit):
    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, limit + 1):
        sum_of_squares += i * i
        square_of_sums += i

    return square_of_sums * square_of_sums - sum_of_squares;

def main():
    result = sumSquareDifference(100)

    print(result)

if __name__ == "__main__":
    main()
