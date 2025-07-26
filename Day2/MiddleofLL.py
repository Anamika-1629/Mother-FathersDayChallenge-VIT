class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l = []
        a = head
        while a:
            l.append(a)
            a = a.next
        if not l:
            return None   
        mid = len(l) // 2
        return l[mid]

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    curr = head
    while curr:
        vals.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(vals))

def main():
    sol = Solution()

    test_lists = [
        [1, 2, 3, 4, 5],     
        [1, 2, 3, 4, 5, 6],  
        [10],                
        []                   
    ]

    for i, vals in enumerate(test_lists, 1):
        head = build_linked_list(vals)
        print(f"Test case {i}: Input list:")
        if head:
            print_linked_list(head)
        else:
            print("(empty list)")
        mid_node = sol.middleNode(head)
        if mid_node:
            print(f"Middle node value: {mid_node.val}\n")
        else:
            print("Middle node: None\n")

if __name__ == "__main__":
    main()
