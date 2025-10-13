class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
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
    def find_node(root, val):
        if not root:
            return None
        if root.val == val:
            return root
        left = Solution.find_node(root.left, val)
        if left:
            return left
        return Solution.find_node(root.right, val)

    @staticmethod
    def main():
        nodes = input().strip()
        vals = nodes.replace('[','').replace(']','').split(',')
        p_val, q_val = map(int, input().strip().split())
        root = Solution.build_tree(nodes)
        p = Solution.find_node(root, p_val)
        q = Solution.find_node(root, q_val)
        sol = Solution()
        lca = sol.lowestCommonAncestor(root, p, q)
        print(lca.val if lca else "null")

if __name__ == "__main__":
    Solution.main()
