class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root

    @staticmethod
    def build_tree(nodes):
        vals = nodes.replace('[','').replace(']','').split(',')
        if not vals or vals[0].strip() == 'null' or vals[0].strip() == '':
            return None
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while queue and i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i].strip() != 'null' and vals[i].strip() != '':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

    @staticmethod
    def printBST(root):
        if root:
            Solution.printBST(root.left)
            print(root.val, end=" ")
            Solution.printBST(root.right)

    @staticmethod
    def main():
        tree = input().strip()
        val = int(input().strip())
        root = Solution.build_tree(tree)
        sol = Solution()
        result = sol.insertIntoBST(root, val)
        Solution.printBST(result)
        print()

if __name__ == "__main__":
    Solution.main()
