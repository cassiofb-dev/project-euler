class Main {
    public static int sumAllMultiplesBellow(int divisor, int limit) {
        int total = 0;

        for (int i = 1; i < limit; i++) {
            if (i % divisor == 0) {
                total += i;
            }
        }

        return total;
    }

    public static int sumAll3And5MultiplesBellow(int limit) {
        int total3 = sumAllMultiplesBellow(3, limit);
        int total5 = sumAllMultiplesBellow(5, limit);
        int total15 = sumAllMultiplesBellow(15, limit);

        return total3 + total5 - total15;
    }

    public static void main(String args[]) {
        int result = sumAll3And5MultiplesBellow(1000);

        System.out.println(result);
    }
}
