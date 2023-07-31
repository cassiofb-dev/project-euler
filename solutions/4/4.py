def isNumberPalindrome(number):
    numberString = str(number)
    reverseNumberString = numberString[::-1]

    return numberString == reverseNumberString

def largestPalindromeProduct(digits):
    lower_limit = 10 ** (digits - 1)
    upper_limit = 10 ** digits

    highest = 0
    product = 0

    for i in range(lower_limit, upper_limit):
        for j in range(lower_limit, upper_limit):
            product = i * j

            if isNumberPalindrome(product) and product > highest:
                highest = product
    return highest

def main():
    result = largestPalindromeProduct(3)

    print(result)

if __name__ == "__main__":
    main()
