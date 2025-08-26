class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    cur = head
    for val in values[1:]:
        cur.next = ListNode(val)
        cur = cur.next
    return head

def print_linked_list(head):
    cur = head
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next
    print(res)

if __name__ == "__main__":
    lst = list(map(int, input("Enter numbers separated by space: ").split()))
    head = build_linked_list(lst)
    sol = Solution()
    result = sol.oddEvenList(head)
    print("Result after odd-even rearrangement:")
    print_linked_list(result)
