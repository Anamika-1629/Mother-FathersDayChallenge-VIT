class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        left_to_right = True
        while queue:
            level = []
            next_queue = []
            for node in queue:
                level.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            queue = next_queue
            left_to_right = not left_to_right
        return result

    @staticmethod
    def build_tree(nodes):
        vals = nodes.split(',')
        if not vals or vals[0] == 'null':
            return None
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1
        while queue and i < len(vals):
            node = queue.pop(0)
            if i < len(vals) and vals[i] != 'null':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if i < len(vals) and vals[i] != 'null':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

    @staticmethod
    def main():
        nodes = input().strip()
        root = Solution.build_tree(nodes)
        sol = Solution()
        print(sol.zigzagLevelOrder(root))

if __name__ == "__main__":
    Solution.main()
