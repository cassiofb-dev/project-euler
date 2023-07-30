class Main {
    public static int largestPrimeFactor(long number) {
        int divisor = 2;

        while (true) {
            while (number % divisor == 0) {
                number = number / divisor;
            }

            if (number == 1) {
                break;
            }

            divisor += 1;
        }

        return divisor;
    }

    public static void main(String args[]) {
        int result = largestPrimeFactor(600851475143L);

        System.out.println(result);
    }
}
