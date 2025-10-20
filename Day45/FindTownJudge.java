import java.util.*;

public class FindTownJudge {
    public int findJudge(int n, int[][] trust) {
        int[] count = new int[n + 1];
        for (int[] t : trust) {
            count[t[0]]--;
            count[t[1]]++;
        }
        for (int i = 1; i <= n; i++) {
            if (count[i] == n - 1) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] trust = new int[m][2];
        for (int i = 0; i < m; i++) {
            trust[i][0] = sc.nextInt();
            trust[i][1] = sc.nextInt();
        }
        System.out.println(new FindTownJudge().findJudge(n, trust));
    }
}
