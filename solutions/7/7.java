class Main {
    public static void fillArray(int[] is_prime, int size, int value) {
        for (int i = 0; i < size; i++) {
            is_prime[i] = value;
        }
    }

    public static int nthPrime(int position) {
        int max_size = 1000000;

        int[] is_prime = new int[max_size];

        fillArray(is_prime, max_size, 1);

        int i, j, prime_position = 0;
        for (i = 2; i < max_size; i++) {
            if (is_prime[i] == 1) {
                prime_position += 1;

                if (prime_position == position) {
                    return i;
                }

                for (j = i * 2; j < max_size; j += i) {
                    is_prime[j] = 0;
                }
            }
        }

    return -1;
}

    public static void main(String args[]) {
        int result = nthPrime(10001);

        System.out.println(result);
    }
}
