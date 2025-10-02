class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(arr):
    if not arr or arr[0] is None:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def sumOfLeftLeaves(root):
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    else:
        total += sumOfLeftLeaves(root.left)
    total += sumOfLeftLeaves(root.right)
    return total

if __name__ == "__main__":
    arr = input("Enter tree (comma separated values, use 'null' for no node): ").split(',')
    arr = [int(x) if x.strip() != 'null' else None for x in arr]
    root = buildTree(arr)
    print(sumOfLeftLeaves(root))
