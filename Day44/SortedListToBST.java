import java.util.*;

public class SortedListToBST {
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) { this.val = val; }
    }
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
    }

    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        if (head.next == null) return new TreeNode(head.val);
        ListNode prev = null, slow = head, fast = head;
        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        if (prev != null) prev.next = null;
        TreeNode root = new TreeNode(slow.val);
        root.left = sortedListToBST(head != slow ? head : null);
        root.right = sortedListToBST(slow.next);
        return root;
    }

    static ListNode buildList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int num : arr) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return dummy.next;
    }

    // For output demonstration (preorder traversal)
    static void preorder(TreeNode root, List<Integer> out) {
        if (root == null) return;
        out.add(root.val);
        preorder(root.left, out);
        preorder(root.right, out);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().replaceAll("[\\[\\]\\s]", "");
        String[] nums = input.split(",");
        int[] arr = new int[nums.length];
        for (int i = 0; i < nums.length; i++)
            arr[i] = Integer.parseInt(nums[i]);
        ListNode head = buildList(arr);
        SortedListToBST sol = new SortedListToBST();
        TreeNode bst = sol.sortedListToBST(head);
        List<Integer> result = new ArrayList<>();
        preorder(bst, result);
        System.out.println(result);
    }
}
