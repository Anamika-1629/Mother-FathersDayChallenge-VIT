class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    """Builds binary tree from a list of values (level order, using None for empty)"""
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

def rightSideView(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                result.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
    return result

if __name__ == "__main__":
    input_str = input("Enter tree nodes in level order (comma separated): ")
    nodes = [int(x) if x != "null" else None for x in input_str.strip().split(',')]
    root = build_tree(nodes)
    print(rightSideView(root))
