import java.util.*;

public class PascalTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<>(Collections.nCopies(rowIndex + 1, 0));
        row.set(0, 1);
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }
        }
        return row;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter rowIndex:");
        int rowIndex = sc.nextInt();
        System.out.println(new PascalTriangleII().getRow(rowIndex));
    }
}
