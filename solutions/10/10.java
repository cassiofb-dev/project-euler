class Main {
    public static void fillArray(int[] is_prime, int size, int value) {
        for (int i = 0; i < size; i++) {
            is_prime[i] = value;
        }
    }

    public static long sumPrimesUntil(int limit) {
       int[] is_prime = new int[limit];

        fillArray(is_prime, limit, 1);

        long prime_sum = 0;
        for (int i = 2; i < limit; i++) {
            if (is_prime[i] == 1) {
                prime_sum += i;

                for (int j = i * 2; j < limit; j += i) {
                    is_prime[j] = 0;
                }
            }
        }

        return prime_sum;
    }

    public static void main(String args[]) {
        long result = sumPrimesUntil(2000000);

        System.out.println(result);
    }
}
