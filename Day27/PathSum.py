class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        left = self.hasPathSum(root.left, targetSum - root.val)
        right = self.hasPathSum(root.right, targetSum - root.val)
        return left or right

def build_tree(nodes):
    if not nodes or nodes[0] == 'null':
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] != 'null':
            current.left = TreeNode(int(nodes[i]))
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] != 'null':
            current.right = TreeNode(int(nodes[i]))
            queue.append(current.right)
        i += 1
    return root

if __name__ == "__main__":
    node_str = input("Enter tree nodes in level order (use 'null' for missing):\n")
    nodes = node_str.strip().split()
    root = build_tree(nodes)
    targetSum = int(input("Enter target sum:\n"))
    sol = Solution()
    print("Path Sum Exists?" , sol.hasPathSum(root, targetSum))
