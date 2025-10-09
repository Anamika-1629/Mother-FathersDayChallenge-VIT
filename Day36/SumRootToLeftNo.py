class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

class Solution(object):
    def sumNumbers(self, root):
        stack = [(root, 0)]
        total = 0
        while stack:
            node, current = stack.pop()
            if node:
                current = current * 10 + node.val
                if not node.left and not node.right:
                    total += current
                else:
                    stack.append((node.right, current))
                    stack.append((node.left, current))
        return total

if __name__ == "__main__":
    inp = input('Enter tree nodes in level order (comma separated, use null for missing): ')
    vals = [int(x) if x != 'null' else None for x in inp.strip().split(',')]
    root = build_tree(vals)
    print(Solution().sumNumbers(root))
