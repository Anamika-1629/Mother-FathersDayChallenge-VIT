import java.util.*;

public class FlippingImage {
    public static int[][] flipAndInvertImage(int[][] img) {
        for (int[] r : img) {
            int l = 0, h = r.length - 1;
            while (l <= h) {
                int tmp = r[l] ^ 1;
                r[l] = r[h] ^ 1;
                r[h] = tmp;
                l++;
                h--;
            }
        }
        return img;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Enter 2D array as rows: e.g., "1 1 0", then next line, "1 0 1", then empty line to end
        List<int[]> matrix = new ArrayList<>();
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            if (line.trim().isEmpty()) break;
            int[] row = Arrays.stream(line.trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            matrix.add(row);
        }
        int[][] img = matrix.toArray(new int[0][]);
        int[][] res = flipAndInvertImage(img);
        for (int[] row : res) {
            System.out.println(Arrays.toString(row));
        }
    }
}
