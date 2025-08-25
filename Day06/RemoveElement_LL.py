# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

def build_linked_list(values):
    head = ListNode(values[0]) if values else None
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

def main():
    sol = Solution()
    test_cases = [
        ([1,2,6,3,4,5,6], 6),
        ([1,2,2,1], 2),
        ([7,7,7,7], 7)
    ]
    for values, val in test_cases:
        head = build_linked_list(values)
        print(f"Original: {values}  remove {val} → ", end="")
        res = sol.removeElements(head, val)
        print_linked_list(res)

if __name__ == "__main__":
    main()
