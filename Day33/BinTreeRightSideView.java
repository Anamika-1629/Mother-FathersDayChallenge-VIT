import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class BinTreeRightSideView {
    public static TreeNode buildTree(String[] vals) {
        if (vals.length == 0 || vals[0].equals("null")) return null;
        TreeNode[] nodes = new TreeNode[vals.length];
        for (int i = 0; i < vals.length; i++) {
            if (!vals[i].equals("null")) {
                nodes[i] = new TreeNode(Integer.parseInt(vals[i]));
            }
        }
        int idx = 1;
        for (int i = 0; i < vals.length && idx < vals.length; i++) {
            if (nodes[i] != null) {
                if (idx < vals.length) nodes[i].left = nodes[idx++];
                if (idx < vals.length) nodes[i].right = nodes[idx++];
            }
        }
        return nodes[0];
    }

    public static List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                if (i == levelSize - 1) result.add(node.val);
                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tree nodes in level order (comma separated): ");
        String[] vals = sc.nextLine().split(",");
        TreeNode root = buildTree(vals);
        System.out.println(rightSideView(root));
    }
}
