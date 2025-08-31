import java.util.Scanner;

class CountOdd {
    public int countOdds(int low, int high) {
        if (low % 2 != 0 || high % 2 != 0) {
            return ((high - low) / 2) + 1;
        } else {
            return (high - low) / 2;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int low = sc.nextInt();
        int high = sc.nextInt();
        CountOdd sol = new CountOdd();
        System.out.println(sol.countOdds(low, high));
        sc.close();
    }
}
