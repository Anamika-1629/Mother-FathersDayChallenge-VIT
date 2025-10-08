# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    # Builds tree from a list, level order with None as 'null'
    if not values or values[0] is None:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

class Solution(object):
    def flatten(self, root):
        curr = root
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right:
                    prev = prev.right
                prev.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right

def print_linked_list(root):
    curr = root
    arr = []
    while curr:
        arr.append(curr.val)
        curr = curr.right
    print(arr)

if __name__ == "__main__":
    inp = input('Enter tree nodes in level order (comma separated, use null for missing): ')
    vals = [int(x) if x != 'null' else None for x in inp.strip().split(',')]
    root = build_tree(vals)
    Solution().flatten(root)
    print_linked_list(root)
