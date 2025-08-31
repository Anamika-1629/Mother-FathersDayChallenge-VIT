class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
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
    def swapNodes(self, head, k):
        first = head
        n = 1
        while n < k:
            first = first.next
            n += 1
        front_node = first
        second = head
        while first.next:
            first = first.next
            second = second.next
        front_node.val, second.val = second.val, front_node.val
        return head

if __name__ == "__main__":
    arr = list(map(int, input("Enter linked list elements (space separated): ").split()))
    k = int(input("Enter k: "))
    head = build_linked_list(arr)
    sol = Solution()
    new_head = sol.swapNodes(head, k)
    print_linked_list(new_head)
