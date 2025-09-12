class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void
        """
        node.val = node.next.val
        node.next = node.next.next

if __name__ == "__main__":
    a, b, c, d = ListNode(4), ListNode(5), ListNode(1), ListNode(9)
    a.next = b
    b.next = c
    c.next = d
    Solution().deleteNode(b)
    curr = a
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()
