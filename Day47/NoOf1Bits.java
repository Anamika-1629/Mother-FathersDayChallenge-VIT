import java.util.*;

public class NoOf1Bits {
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            n = n & (n - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        NoOf1Bits sol = new NoOf1Bits();
        System.out.println(sol.hammingWeight(n));
    }
}
