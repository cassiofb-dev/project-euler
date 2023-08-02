class Main {
    public static int sumSquareDifference(int limit) {
        int sum_of_squares = 0;
        int square_of_sums = 0;

        for (int i = 1; i <= limit; i++) {
            sum_of_squares += i * i;
            square_of_sums += i;
        }

        return square_of_sums * square_of_sums - sum_of_squares;
    }

    public static void main(String args[]) {
        int result = sumSquareDifference(100);

        System.out.println(result);
    }
}
