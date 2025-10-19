class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if head != slow else None)
        root.right = self.sortedListToBST(slow.next)
        return root

def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def preorder(node, lst):
    if not node: return
    lst.append(node.val)
    preorder(node.left, lst)
    preorder(node.right, lst)

if __name__ == "__main__":
    arr = input().strip().strip("[]").split(",")
    arr = [int(x) for x in arr if x != '']
    head = build_list(arr)
    sol = Solution()
    bst = sol.sortedListToBST(head)
    result = []
    preorder(bst, result)
    print(result)
