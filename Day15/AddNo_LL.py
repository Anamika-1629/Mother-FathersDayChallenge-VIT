class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy_head.next

def make_list(lst):
    dummy = ListNode()
    cur = dummy
    for num in lst:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

if __name__ == "__main__":
    l1 = make_list([2,4,3])
    l2 = make_list([5,6,4])
    result = Solution().addTwoNumbers(l1, l2)
    print_list(result)
