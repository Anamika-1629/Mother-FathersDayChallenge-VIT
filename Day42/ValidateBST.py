class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        stack = []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev is not None and root.val <= prev:
                return False
            prev = root.val
            root = root.right
        return True

def build_tree(values):
    # Builds tree from list, index-based (same as LeetCode layer order)
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    arr = input().strip()
    arr = arr.strip("[]").split(",")
    arr = [int(x) if x != "null" else None for x in arr]
    root = build_tree(arr)
    sol = Solution()
    print(sol.isValidBST(root))
