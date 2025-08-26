# Coding Challenge Solutions


This repository contains solutions to Day 8 problems.


---


## 1. Excel Sheet Column Number (LeetCode 171)


**Problem:**  
Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return its corresponding column number.

**Constraints:**  
- `1 <= columnTitle.length <= 7`
- `columnTitle` consists only of uppercase English letters.

**Approach:**  
- Traverse the string from right to left.
- Convert each character to its position in the alphabet (A=1, B=2, ..., Z=26).
- Calculate the column number by summing each position value multiplied by 26 raised to the power of its digit index.
- Return the computed sum as the column number.

**Complexity:**  
- Time: O(n), where n is the length of `columnTitle`.
- Space: O(1), only constant extra space used.

---


## 2. Odd Even Linked List (LeetCode 328)


**Problem:**  
Given the `head` of a singly linked list, group all nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, the second node is even, and so on.

**Constraints:**  
- The number of nodes in the list is in the range `[0, 10^4]`.
- `-10^6 <= Node.val <= 10^6`

**Approach:**  
- Return the list immediately if it has less than two nodes.
- Initialize pointers for odd nodes and even nodes starting at the first and second node respectively.
- Iterate through the list, linking odd nodes together and even nodes together separately.
- After processing, link the last odd node to the head of the even node list.
- Return the reordered list.

**Complexity:**  
- Time: O(n), where n is the number of nodes in the list.
- Space: O(1), the operation is done in place without extra memory.

---
