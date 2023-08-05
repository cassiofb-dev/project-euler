import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

class Main {
    public static String getSeries() throws IOException {
        Path file_name = Path.of("solutions/8/series.txt");

        String file_contents = Files.readString(file_name);

        return file_contents;
    }

    public static long largestProductInSeries(int adjacents) throws IOException {
        String series = getSeries();

        long largest_product = 1;
        long current_product = 1;
        for (int i = 0; i < series.length() - adjacents; i++) {
            for (int j = 0; j < adjacents; j++) {
                int number = series.charAt(i + j) - '0';
                current_product *= number;
            }

            if (current_product > largest_product) {
                largest_product = current_product;
            }

            current_product = 1;
        }

        return largest_product;
    }

    public static void main(String args[]) throws IOException {
        long result = largestProductInSeries(13);

        System.out.println(result);
    }
}
