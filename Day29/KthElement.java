import java.util.*;

public class KthElement {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().trim().split(" ");
        int n = arr.length;
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(arr[i]);
        int k = sc.nextInt();
        System.out.println(findKthLargest(nums, k));
    }

    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int n : nums) {
            heap.add(n);
            if (heap.size() > k)
                heap.poll();
        }
        return heap.peek();
    }
}
