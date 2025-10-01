class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

def build_tree(nodes):
    if not nodes or nodes[0] == 'null':
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if nodes[i] != 'null':
            curr.left = TreeNode(int(nodes[i]))
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] != 'null':
            curr.right = TreeNode(int(nodes[i]))
            queue.append(curr.right)
        i += 1
    return root

if __name__ == "__main__":
    node_str = input("Enter tree nodes in level order (use 'null' for missing):\n")
    nodes = node_str.strip().split()
    root = build_tree(nodes)
    sol = Solution()
    print("Minimum Depth of Binary Tree:", sol.minDepth(root))
