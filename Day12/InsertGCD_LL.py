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
    def insertGreatestCommonDivisors(self, head):
        current = head
        while current and current.next:
            a, b = current.val, current.next.val
            # Compute GCD
            while b != 0:
                a, b = b, a % b
            g = a
            # Create and insert new GCD node
            new_node = ListNode(g)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        return head

if __name__ == "__main__":
    arr = list(map(int, input("Enter list elements (space separated): ").split()))
    head = build_linked_list(arr)
    sol = Solution()
    new_head = sol.insertGreatestCommonDivisors(head)
    print_linked_list(new_head)
