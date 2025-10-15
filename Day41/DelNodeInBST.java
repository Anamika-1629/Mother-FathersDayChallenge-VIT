import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int x) { val = x; }
}

public class DelNodeInBST {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (key < root.val) {
            root.left = deleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = deleteNode(root.right, key);
        } else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            TreeNode temp = root.right;
            while (temp.left != null) {
                temp = temp.left;
            }
            root.val = temp.val;
            root.right = deleteNode(root.right, temp.val);
        }
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
        int key = sc.nextInt();
        TreeNode root = buildTree(vals);
        DelNodeInBST sol = new DelNodeInBST();
        TreeNode result = sol.deleteNode(root, key);
        printBST(result);
        System.out.println();
    }
}
