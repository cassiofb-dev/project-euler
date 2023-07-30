def sumAllMultiplesBellow(divisor, limit):
    total = 0

    for i in range(1, limit):
        if (i % divisor == 0):
            total += i

    return total

def sumAll3And5MultiplesBellow(limit):
    total3 = sumAllMultiplesBellow(3, limit)
    total5 = sumAllMultiplesBellow(5, limit)
    total15 = sumAllMultiplesBellow(15, limit)

    return total3 + total5 - total15

def main():
    result = sumAll3And5MultiplesBellow(1000)

    print(result)

if __name__ == '__main__':
    main()
