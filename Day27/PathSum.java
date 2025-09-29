import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class PathSum {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) return root.val == targetSum;
        return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
    }

    public static TreeNode buildTree(String[] nodes) {
        if (nodes.length == 0 || nodes[0].equals("null")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int i = 1;
        while (queue.size() > 0 && i < nodes.length) {
            TreeNode current = queue.poll();
            if (i < nodes.length && !nodes[i].equals("null")) {
                current.left = new TreeNode(Integer.parseInt(nodes[i]));
                queue.add(current.left);
            }
            i++;
            if (i < nodes.length && !nodes[i].equals("null")) {
                current.right = new TreeNode(Integer.parseInt(nodes[i]));
                queue.add(current.right);
            }
            i++;
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter tree nodes in level order (use 'null' for missing):");
        String[] nodes = sc.nextLine().split(" ");
        TreeNode root = buildTree(nodes);
        System.out.println("Enter target sum:");
        int targetSum = sc.nextInt();
        PathSum sol = new PathSum();
        System.out.println("Path Sum Exists? " + sol.hasPathSum(root, targetSum));
        sc.close();
    }
}
