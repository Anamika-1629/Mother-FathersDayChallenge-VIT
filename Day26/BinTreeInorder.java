import java.util.*;

class TreeNode {
    int val;
    TreeNode left, right;
    TreeNode(int val) { this.val = val; }
}

class BinTreeInorder {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode curr = root;

        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            result.add(curr.val);
            curr = curr.right;
        }

        return result;
    }

    // Helper to construct tree from level order input, treating -1 as null
    public static TreeNode buildTree(List<Integer> nodes) {
        if(nodes.isEmpty() || nodes.get(0) == -1) return null;
        TreeNode root = new TreeNode(nodes.get(0));
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int i = 1;
        while(i < nodes.size()) {
            TreeNode curr = q.poll();
            Integer leftVal = nodes.get(i++);
            if(leftVal != -1) {
                curr.left = new TreeNode(leftVal);
                q.add(curr.left);
            }
            if(i < nodes.size()) {
                Integer rightVal = nodes.get(i++);
                if(rightVal != -1) {
                    curr.right = new TreeNode(rightVal);
                    q.add(curr.right);
                }
            }
        }
        return root;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of nodes (including nulls as -1):");
        int n = sc.nextInt();
        System.out.println("Enter nodes in level order (use -1 for null):");
        List<Integer> nodes = new ArrayList<>();
        for(int i = 0; i < n; i++) {
            nodes.add(sc.nextInt());
        }
        TreeNode root = buildTree(nodes);
        BinTreeInorder sol = new BinTreeInorder();
        List<Integer> result = sol.inorderTraversal(root);
        System.out.println("Inorder traversal:");
        System.out.println(result);
    }
}
