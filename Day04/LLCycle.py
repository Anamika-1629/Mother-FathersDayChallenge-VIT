class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow is not fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

def main():
    solution = Solution()

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2 

    node5 = ListNode(1)
    node6 = ListNode(2)
    node5.next = node6
    
    print("Has cycle (expected True):", solution.hasCycle(node1))
    print("Has cycle (expected False):", solution.hasCycle(node5))

if __name__ == "__main__":
    main()