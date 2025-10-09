import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int v) { val = v; }
}

class Pair<K, V> {
    private K key;
    private V value;
    public Pair(K key, V value) { this.key = key; this.value = value; }
    public K getKey() { return key; }
    public V getValue() { return value; }
}

public class SumRootToLeftNo {
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
    public int sumNumbers(TreeNode root) {
        Stack<Pair<TreeNode, Integer>> stack = new Stack<>();
        stack.push(new Pair<>(root, 0));
        int total = 0;
        while (!stack.isEmpty()) {
            Pair<TreeNode, Integer> pair = stack.pop();
            TreeNode node = pair.getKey();
            int current = pair.getValue();
            if (node != null) {
                current = current * 10 + node.val;
                if (node.left == null && node.right == null) {
                    total += current;
                } else {
                    stack.push(new Pair<>(node.right, current));
                    stack.push(new Pair<>(node.left, current));
                }
            }
        }
        return total;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter tree nodes in level order (comma separated, use null for missing): ");
        String[] vals = sc.nextLine().split(",");
        TreeNode root = buildTree(vals);
        SumRootToLeftNo solution = new SumRootToLeftNo();
        System.out.println(solution.sumNumbers(root));
    }
}
