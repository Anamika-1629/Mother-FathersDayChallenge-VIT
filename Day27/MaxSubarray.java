import java.util.Scanner;

class MaxSubarray {
    public int maxSubArray(int[] nums) {
        int curr = nums[0], res = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curr = Math.max(nums[i], curr + nums[i]);
            res = Math.max(res, curr);
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements:");
        int n = sc.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        MaxSubarray sol = new MaxSubarray();
        System.out.println(sol.maxSubArray(nums));
        sc.close();
    }
}
