# Coding Challenge Solutions

Day 44 problems.

---

## 1. Maximum Number of Vowels in a Substring of Given Length

**Problem:**  
Given a string `s` and an integer `k`, return the maximum number of vowel letters in any substring of `s` with length `k`.

**Constraints:**  
- Vowel letters are 'a', 'e', 'i', 'o', and 'u'.
- `1 ≤ k ≤ s.length ≤ 10^5`
- `s` consists of lowercase English letters.

**Approach:**  
- Use the sliding window technique to maintain a window of length `k`.
- Count vowels in the current window, moving the window one character at a time.
- For each move, subtract the count if the outgoing character is a vowel and add if the incoming one is.
- Track the maximum vowel count seen.

**Complexity:**  
- Time: O(n), where n is the length of the string `s`.
- Space: O(1), as only counters are used.

---

## 2. Convert Sorted List to Binary Search Tree

**Problem:**  
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.

**Constraints:**  
- The linked list nodes are in non-decreasing order.
- The number of nodes is in the range `[0, 2 * 10^4]`.

**Approach:**  
- Use fast and slow pointers to find the middle node, which will be the root of the BST.
- Recursively repeat this process for the left and right halves of the list to build left and right subtrees.
- Disconnect the left part from the middle to form sublists during recursion.

**Complexity:**  
- Time: O(n log n), as each list-to-tree level divides the list and traverses nodes to find the middle.
- Space: O(log n), due to recursion stack.

---
