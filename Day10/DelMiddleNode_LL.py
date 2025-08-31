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
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

if __name__ == "__main__":
    arr = list(map(int, input("Enter list elements (space separated): ").split()))
    head = build_linked_list(arr)
    sol = Solution()
    new_head = sol.deleteMiddle(head)
    print_linked_list(new_head)
