import java.util.*;

class CountPrimes {
    public int countPrimes(int n) {
        if (n < 2) return 0;
        boolean[] isPrime = new boolean[n];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i < n; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j < n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        int count = 0;
        for (boolean b : isPrime) {
            if (b) count++;
        }
        return count;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        CountPrimes sol = new CountPrimes();
        System.out.println(sol.countPrimes(n));
    }
}
