import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class PrimeNoOfSetBit_BinRep {
    public int countPrimeSetBits(int left, int right) {
        Set<Integer> primes = new HashSet<>(Arrays.asList(
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31
        ));

        int count = 0;
        for (int i = left; i <= right; i++) {
            int bits = Integer.bitCount(i);
            if (primes.contains(bits)) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- 762. Prime Number of Set Bits (Java) ---");
        
        System.out.print("Enter the left bound (integer): ");
        int left = scanner.nextInt();
        
        System.out.print("Enter the right bound (integer): ");
        int right = scanner.nextInt();

        PrimeNoOfSetBit_BinRep solution = new PrimeNoOfSetBit_BinRep();
        int result = solution.countPrimeSetBits(left, right);

        System.out.println("\nInput: left = " + left + ", right = " + right);
        System.out.println("Output (Count of numbers with prime set bits): " + result);

        scanner.close();
    }
}