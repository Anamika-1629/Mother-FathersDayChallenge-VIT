class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

def build_tree(nodes):
    if not nodes or nodes[0] == None:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
        current = queue.pop(0)
        if current:
            left_val = nodes[i] if i < len(nodes) else None
            if left_val is not None:
                current.left = TreeNode(left_val) if left_val is not None else None
            queue.append(current.left)
            i += 1
            
            right_val = nodes[i] if i < len(nodes) else None
            if right_val is not None:
                current.right = TreeNode(right_val) if right_val is not None else None
            queue.append(current.right)
            i += 1
    return root

if __name__ == "__main__":
    n = int(input("Enter number of nodes (including 'None'): "))
    nodes_input = input("Enter nodes in level order (use None for null): ")
    nodes = [int(x) if x != 'None' else None for x in nodes_input.split()]
    root = build_tree(nodes)
    sol = Solution()
    print("Inorder traversal:", sol.inorderTraversal(root))
