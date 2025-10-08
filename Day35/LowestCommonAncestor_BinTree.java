import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class LowestCommonAncestor_BinTree {
    public static TreeNode buildTree(String[] vals) {
        if (vals.length == 0 || vals[0].equals("null")) return null;
        TreeNode[] nodes = new TreeNode[vals.length];
        for (int i = 0; i < vals.length; i++) {
            if (!vals[i].equals("null")) nodes[i] = new TreeNode(Integer.parseInt(vals[i]));
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
    public static TreeNode findNode(TreeNode root, int val) {
        if (root == null) return null;
        if (root.val == val) return root;
        TreeNode left = findNode(root.left, val);
        if (left != null) return left;
        return findNode(root.right, val);
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root == p || root == q) return root;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if (left != null && right != null) return root;
        return left != null ? left : right;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tree nodes in level order (comma separated, use null for missing): ");
        String[] vals = sc.nextLine().split(",");
        TreeNode root = buildTree(vals);
        System.out.print("Enter value of p: ");
        int pVal = sc.nextInt();
        System.out.print("Enter value of q: ");
        int qVal = sc.nextInt();
        TreeNode p = findNode(root, pVal);
        TreeNode q = findNode(root, qVal);
        LowestCommonAncestor_BinTree sol = new LowestCommonAncestor_BinTree();
        TreeNode lca = sol.lowestCommonAncestor(root, p, q);
        System.out.println("LCA value: " + lca.val);
    }
}
