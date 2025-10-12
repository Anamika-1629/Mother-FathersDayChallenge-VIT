class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    @staticmethod
    def build_tree(nodes):
        vals = nodes.replace('[','').replace(']','').split(',')
        if not vals or vals[0] == 'null' or vals[0] == '':
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
        nodes = input().strip()
        val = int(input().strip())
        root = Solution.build_tree(nodes)
        sol = Solution()
        res = sol.searchBST(root, val)
        Solution.printBST(res)
        print()

if __name__ == "__main__":
    Solution.main()
