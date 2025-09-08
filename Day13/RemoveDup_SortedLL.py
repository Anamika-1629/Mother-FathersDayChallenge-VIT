class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next

def list_to_linked(lst):
    dummy = ListNode(0)
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    head = list_to_linked(nums)
    new_head = Solution().deleteDuplicates(head)
    print(linked_to_list(new_head))
