import java.util.*;

public class RotateImage {
    public static void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n / 2; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n - 1 - j];
                matrix[i][n - 1 - j] = temp;
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Input: each row as space-separated values, end with empty line
        List<int[]> matrixList = new ArrayList<>();
        while(sc.hasNextLine()) {
            String line = sc.nextLine();
            if (line.trim().isEmpty()) break;
            int[] row = Arrays.stream(line.trim().replaceAll("[\\[\\]]", "").split(","))
                              .map(String::trim)
                              .mapToInt(Integer::parseInt)
                              .toArray();
            matrixList.add(row);
        }
        int[][] matrix = matrixList.toArray(new int[0][]);
        rotate(matrix);
        for (int[] row : matrix) {
            System.out.println(Arrays.toString(row));
        }
    }
}
