class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        before_head = ListNode(0)
        before = before_head
        after_head = ListNode(0)
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next

def build_linked_list(values):
    head = ListNode(values)
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print("[" + ",".join(res) + "]")

if __name__ == "__main__":
    arr = list(map(int, input().strip('[]\n').split(',')))
    x = int(input())
    head = build_linked_list(arr)
    sol = Solution()
    result = sol.partition(head, x)
    print_linked_list(result)
