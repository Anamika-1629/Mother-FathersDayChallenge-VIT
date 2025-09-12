import java.util.Scanner;

public class SqNoSum {
    public boolean judgeSquareSum(int c) {
        for (int a = 0; a <= Math.sqrt(c); a++) {
            int b_sq = c - (a * a);
            int b = (int) Math.sqrt(b_sq);
            if (b * b == b_sq) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int c = scanner.nextInt();
        SqNoSum sol = new SqNoSum();
        System.out.println(sol.judgeSquareSum(c));
        scanner.close();
    }
}
