import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class LowestCommonAncestorOfBST {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (p.val < root.val && q.val < root.val)
            return lowestCommonAncestor(root.left, p, q);
        else if (p.val > root.val && q.val > root.val)
            return lowestCommonAncestor(root.right, p, q);
        else
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

    public static TreeNode findNode(TreeNode root, int val) {
        if (root == null) return null;
        if (root.val == val) return root;
        TreeNode left = findNode(root.left, val);
        if (left != null) return left;
        return findNode(root.right, val);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine().replaceAll("[\\[\\]]", "");
        String[] vals = input.split(",");
        int pVal = sc.nextInt();
        int qVal = sc.nextInt();
        TreeNode root = buildTree(vals);
        TreeNode p = findNode(root, pVal);
        TreeNode q = findNode(root, qVal);
        LowestCommonAncestorOfBST sol = new LowestCommonAncestorOfBST();
        TreeNode lca = sol.lowestCommonAncestor(root, p, q);
        System.out.println(lca != null ? lca.val : "null");
    }
}
