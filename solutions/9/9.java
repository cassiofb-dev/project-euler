import java.lang.Math;

class Main {
    public static boolean isInteger(double number) {
        return Math.floor(number) == number;
    }

    public static int specialPythagoreanTriplet(int triplet_sum) {
        for (int a = 1; a < triplet_sum; a++) {
            for (int b = a + 1; b < triplet_sum - a; b++) {
                double c = Math.sqrt(a * a + b * b);

                if (isInteger(c) && (int) (a + b + c) == triplet_sum) {
                    return (int) (a * b * c);
                }
            }
        }

        return -1;
    }

    public static void main(String args[]) {
        int result = specialPythagoreanTriplet(1000);

        System.out.println(result);
    }
}
