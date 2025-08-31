import java.util.Scanner;

class FacTrailingZeros {
    public int trailingZeroes(int n) {
        int count = 0;
        while (n >= 5) {
            n /= 5;
            count += n;
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        FacTrailingZeros sol = new FacTrailingZeros();
        System.out.println(sol.trailingZeroes(n));
        sc.close();
    }
}
