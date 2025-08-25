# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head      
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        k = k % length
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        return new_head

# Helper to build linked list from python list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print linked list values
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    print(values)

def main():
    sol = Solution()

    # Example: rotate [1,2,3,4,5] by 2 steps → [4,5,1,2,3]
    values = [1, 2, 3, 4, 5]
    k = 2
    print("Original list:", values)
    head = build_linked_list(values)
    rotated_head = sol.rotateRight(head, k)
    print(f"List after rotating by {k}: ", end="")
    print_linked_list(rotated_head)

if __name__ == "__main__":
    main()
