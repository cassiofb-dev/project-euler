def nthPrime(position):
    max_size = 1000000

    is_prime = [1] * max_size

    prime_position = 0
    for i in range(2, max_size):
        if (is_prime[i] == 1):
            prime_position += 1

            if (prime_position == position):
                return i

            for j in range(i * 2, max_size, i):
                is_prime[j] = 0
    return -1

def main():
    result = nthPrime(10001)
    print(result)

if __name__ == "__main__":
    main()
