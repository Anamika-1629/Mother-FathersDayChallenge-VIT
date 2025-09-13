import java.util.Scanner;

class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int[] out_list = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int temp = nums[i] + nums[j];
                if (temp == target) {
                    out_list[0] = i;
                    out_list[1] = j;
                    return out_list;
                }
            }
        }
        return out_list;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Array size: ");
        int n = sc.nextInt();
        int[] nums = new int[n];
        System.out.println("Enter array elements: ");
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }
        System.out.print("Enter target: ");
        int target = sc.nextInt();

        TwoSum sol = new TwoSum(); 
        int[] result = sol.twoSum(nums, target);

        System.out.println("Indices: " + result[0] + ", " + result[1]);
    }
}
