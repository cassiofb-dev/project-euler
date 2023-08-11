def sumPrimesUntil(limit):
    is_prime = [1] * limit

    prime_sum = 0
    for i in range(2, limit):
        if (is_prime[i] == 1):
            prime_sum += i

            for j in range(i * 2, limit, i):
                is_prime[j] = 0
    return prime_sum

def main():
    result = sumPrimesUntil(2000000)

    print(result)

if __name__ == "__main__":
    main()
