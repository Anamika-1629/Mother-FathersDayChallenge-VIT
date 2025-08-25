# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare first half and reversed second half
        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True

# Helper: build a linked list from a python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def main():
    sol = Solution()

    # Example test cases
    case1 = build_linked_list([1, 2, 2, 1])
    case2 = build_linked_list([1, 2])
    case3 = build_linked_list([1, 2, 3, 2, 1])

    print("Case [1,2,2,1] ->", sol.isPalindrome(case1))  # True
    print("Case [1,2] ->", sol.isPalindrome(case2))      # False
    print("Case [1,2,3,2,1] ->", sol.isPalindrome(case3)) # True

if __name__ == "__main__":
    main()
