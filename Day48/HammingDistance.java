import java.util.*;

public class HammingDistance {
    public int hammingDistance(int x, int y) {
        int xor = x ^ y, count = 0;
        while (xor != 0) {
            xor &= xor - 1;
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        HammingDistance sol = new HammingDistance();
        System.out.println(sol.hammingDistance(x, y));
    }
}
