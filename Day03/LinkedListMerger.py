class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next

def create_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for num in lst[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

def main():
    solution = Solution()

    list1 = create_list([1, 3, 5])
    list2 = create_list([2, 4, 6])
    merged = solution.mergeTwoLists(list1, list2)
    print_list(merged)

    list1 = create_list([1, 2, 4])
    list2 = create_list([1, 3, 4])
    merged = solution.mergeTwoLists(list1, list2)
    print_list(merged)  

if __name__ == "__main__":
    main()