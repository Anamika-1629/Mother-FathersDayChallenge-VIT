import java.util.*;

public class GoodArrayCheck {
    public boolean isGoodArray(int[] nums) {
        int gcd = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int a = gcd, b = nums[i];
            while (b != 0) {
                int temp = a % b;
                a = b;
                b = temp;
            }
            gcd = a;
            if (gcd == 1) return true;
        }
        return gcd == 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] parts = sc.nextLine().replaceAll("[\\[\\]\\s]", "").split(",");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) 
            nums[i] = Integer.parseInt(parts[i]);
        GoodArrayCheck sol = new GoodArrayCheck();
        System.out.println(sol.isGoodArray(nums));
    }
}
