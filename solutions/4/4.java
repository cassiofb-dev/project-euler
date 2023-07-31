import java.lang.Math;

class Main {
    public static boolean isNumberPalindrome(int number) {
        String numberString = String.valueOf(number);
        String reverseNumberString = new StringBuilder(numberString).reverse().toString();

        return numberString.equals(reverseNumberString);
    }

    public static int largestPalindromeProduct(int digits) {
        int lower_limit = (int) Math.pow(10, digits - 1);
        int upper_limit = (int) Math.pow(10, digits);

        int highest = 0;
        int product;

        for (int i = lower_limit; i < upper_limit; i++) {
            for (int j = lower_limit; j < upper_limit; j++) {
                product = i * j;

                if (isNumberPalindrome(product) && product > highest) {
                    highest = product;
                }
            }
        }

        return highest;
    }

    public static void main(String args[]) {
        int result = largestPalindromeProduct(3);

        System.out.println(result);
    }
}
