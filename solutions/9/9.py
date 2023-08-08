import math

def specialPythagoreanTriplet(triplet_sum):
    for a in range (1, triplet_sum):
        for b in range(a + 1, triplet_sum - a):
            c = math.sqrt(a * a + b * b)

            if (c.is_integer() and a + b + c == triplet_sum):
                return a * b * c

    return -1

def main():
    result = specialPythagoreanTriplet(1000)

    print(result)

if __name__ == "__main__":
    main()
