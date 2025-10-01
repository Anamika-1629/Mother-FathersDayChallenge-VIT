import java.util.*;

class SubarrayLCM {
    public int subarrayLCM(int[] nums, int k) {
        int count = 0, n = nums.length;
        for (int i = 0; i < n; i++) {
            int curr = nums[i];
            if (curr > k || k % curr != 0) continue;
            for (int j = i; j < n; j++) {
                if (i != j) {
                    int a = curr, b = nums[j];
                    while (b != 0) {
                        int temp = b;
                        b = a % b;
                        a = temp;
                    }
                    curr = (curr * nums[j]) / a;
                }
                if (curr == k) count++;
                else if (curr > k) break;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of elements:");
        int n = sc.nextInt();
        int[] nums = new int[n];

        System.out.println("Enter array elements:");
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();

        System.out.println("Enter k:");
        int k = sc.nextInt();

        SubarrayLCM sol = new SubarrayLCM();
        System.out.println("Number of subarrays with LCM equal to k: " + sol.subarrayLCM(nums, k));
        sc.close();
    }
}
