import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

public class BinTreeLevelOrder {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> level = new ArrayList<>();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                level.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(level);
        }
        return result;
    }

    // Helper to build tree from input
    static TreeNode buildTree(String[] arr) {
        if (arr.length == 0 || arr[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int i = 1;
        while (i < arr.length) {
            TreeNode curr = queue.poll();
            if (!arr[i].equals("null")) {
                curr.left = new TreeNode(Integer.parseInt(arr[i]));
                queue.add(curr.left);
            }
            i++;
            if (i < arr.length && !arr[i].equals("null")) {
                curr.right = new TreeNode(Integer.parseInt(arr[i]));
                queue.add(curr.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] arr = sc.nextLine().replaceAll("[\\[\\]]", "").split(",");
        for(int i = 0; i < arr.length; i++) arr[i] = arr[i].trim();
        TreeNode root = buildTree(arr);
        List<List<Integer>> result = levelOrder(root);
        System.out.println(result);
    }
}
