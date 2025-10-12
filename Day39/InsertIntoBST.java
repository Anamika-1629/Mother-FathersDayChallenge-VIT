import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

public class InsertIntoBST {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        if (val < root.val) root.left = insertIntoBST(root.left, val);
        else root.right = insertIntoBST(root.right, val);
        return root;
    }

    public static TreeNode buildTree(String[] vals) {
        if (vals.length == 0 || vals[0].equals("null") || vals[0].equals("")) return null;
        TreeNode root = new TreeNode(Integer.parseInt(vals[0].trim()));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        int i = 1;
        while (!queue.isEmpty() && i < vals.length) {
            TreeNode node = queue.poll();
            if (i < vals.length && !vals[i].trim().equals("null") && !vals[i].trim().equals("")) {
                node.left = new TreeNode(Integer.parseInt(vals[i].trim()));
                queue.offer(node.left);
            }
            i++;
            if (i < vals.length && !vals[i].trim().equals("null") && !vals[i].trim().equals("")) {
                node.right = new TreeNode(Integer.parseInt(vals[i].trim()));
                queue.offer(node.right);
            }
            i++;
        }
        return root;
    }

    public static void printBST(TreeNode root) {
        if (root == null) return;
        printBST(root.left);
        System.out.print(root.val + " ");
        printBST(root.right);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().replaceAll("[\\[\\]]", "");
        String[] vals = input.split(",");
        int val = sc.nextInt();
        TreeNode root = buildTree(vals);
        InsertIntoBST sol = new InsertIntoBST();
        TreeNode result = sol.insertIntoBST(root, val);
        printBST(result);
        System.out.println();
    }
}
