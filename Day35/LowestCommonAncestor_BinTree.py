class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(values):
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right

if __name__ == "__main__":
    inp = input("Enter tree nodes in level order (comma separated, use null for missing): ")
    nodes = [int(x) if x != 'null' else None for x in inp.strip().split(',')]
    root = build_tree(nodes)
    p_val = int(input("Enter value of p: "))
    q_val = int(input("Enter value of q: "))
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    lca = Solution().lowestCommonAncestor(root, p, q)
    print("LCA value:", lca.val)
