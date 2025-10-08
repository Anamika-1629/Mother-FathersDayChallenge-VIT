import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

public class FlattenBinTreeToLL {
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

    public void flatten(TreeNode root) {
        TreeNode curr = root;
        while (curr != null) {
            if (curr.left != null) {
                TreeNode prev = curr.left;
                while (prev.right != null) {
                    prev = prev.right;
                }
                prev.right = curr.right;
                curr.right = curr.left;
                curr.left = null;
            }
            curr = curr.right;
        }
    }

    public static void printRightList(TreeNode root) {
        TreeNode curr = root;
        List<Integer> result = new ArrayList<>();
        while (curr != null) {
            result.add(curr.val);
            curr = curr.right;
        }
        System.out.println(result);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tree nodes in level order (comma separated, use null for missing): ");
        String[] vals = sc.nextLine().split(",");
        TreeNode root = buildTree(vals);
        FlattenBinTreeToLL solution = new FlattenBinTreeToLL();
        solution.flatten(root);
        printRightList(root);
    }
}
