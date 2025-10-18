class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                print(root.val)
                return root.val
            root = root.right

def build_tree(values):
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    arr = input().strip().strip("[]").split(",")
    arr = [int(x) if x != "null" else None for x in arr]
    k = int(input().strip())
    root = build_tree(arr)
    sol = Solution()
    sol.kthSmallest(root, k)
