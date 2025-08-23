# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

def printList(head):
    curr = head
    res = []
    while curr:
        res.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(res))

def main():
    # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print("Original Linked List:")
    printList(head)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    print("Reversed Linked List:")
    printList(reversed_head)

if __name__ == "__main__":
    main()
