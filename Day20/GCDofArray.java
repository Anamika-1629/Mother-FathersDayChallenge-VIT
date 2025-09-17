import java.util.*;

public class GCDofArray {
    public int findGCD(int[] nums) {
        int min = nums[0];
        int max = nums[0];
        for (int num : nums) {
            if (num < min) min = num;
            if (num > max) max = num;
        }
        for (int i = min; i >= 1; i--) {
            if (min % i == 0 && max % i == 0) {
                return i;
            }
        }
        return 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter numbers separated by spaces:");
        String[] parts = sc.nextLine().split(" ");
        int[] nums = Arrays.stream(parts).mapToInt(Integer::parseInt).toArray();
        System.out.println(new GCDofArray().findGCD(nums));
    }
}
