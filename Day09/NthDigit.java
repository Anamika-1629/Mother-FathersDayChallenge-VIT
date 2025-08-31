import java.util.Scanner;

public class NthDigit {
    public int findNthDigit(int n) {
        int length = 1;
        long count = 9;
        int start = 1;

        while (n > length * count) {
            n -= length * count;
            length += 1;
            count *= 10;
            start *= 10;
        }
        start += (n - 1) / length;
        String s = Integer.toString(start);
        return s.charAt((n - 1) % length) - '0';
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        NthDigit sol = new NthDigit();
        System.out.println(sol.findNthDigit(n));
        sc.close();
    }
}
