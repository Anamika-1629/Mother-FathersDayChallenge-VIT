class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(lst):
    head = ListNode(lst[0])
    curr = head
    for v in lst[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("[" + ", ".join(res) + "]")

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next

if __name__ == "__main__":
    arr = list(map(int, input("Enter list elements (space separated): ").split()))
    n = int(input("Enter n: "))
    head = build_linked_list(arr)
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    print_linked_list(new_head)
