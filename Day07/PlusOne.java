import java.util.Scanner;

public class PlusOne {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1; i >= 0; i--) {
            digits[i]++;
            digits[i] %= 10;
            if (digits[i] != 0) {
                return digits;
            }
        }
        int[] result = new int[digits.length + 1];
        result[0] = 1;
        return result;
    }

    public static void main(String[] args) {
        PlusOne sol = new PlusOne();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the digits array: ");
        int n = scanner.nextInt();

        int[] digits = new int[n];
        System.out.println("Enter the digits:");
        for (int i = 0; i < n; i++) {
            digits[i] = scanner.nextInt();
        }
        
        int[] result = sol.plusOne(digits);

        System.out.print("Result after plus one: ");
        for (int digit : result) {
            System.out.print(digit + " ");
        }
        System.out.println();

        scanner.close();
    }
}
