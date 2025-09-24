import java.util.*;

public class MoveZeroes {
    public void moveZeroes(int[] nums) {
        int i = 0;
        int count = 0;
        int n = nums.length;
        List<Integer> list = new ArrayList<>();
        for (int num : nums)
            list.add(num);

        while (i < list.size() - count) {
            if (list.get(i) == 0) {
                list.remove(i);
                list.add(0);
                count++;
            } else {
                i++;
            }
        }
        for (int j = 0; j < n; j++)
            nums[j] = list.get(j);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter numbers separated by spaces: ");
        String[] parts = sc.nextLine().split(" ");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++)
            nums[i] = Integer.parseInt(parts[i]);
        new MoveZeroes().moveZeroes(nums);
        System.out.println(Arrays.toString(nums));
    }
}
