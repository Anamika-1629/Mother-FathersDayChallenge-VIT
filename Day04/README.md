# Coding Challenge Solutions

Day 4 problems.

---

## 1. Palindrome Number (LeetCode 9)

**Problem:**  
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

**Approach:**  
- Convert the integer to a string for easy comparison  
- Create two strings:  
  - One built by iterating forward through the digits  
  - One built by iterating backward through the digits  
- Compare the two strings for equality  
- Return true if they match, false otherwise  

**Complexity:**  
- Time: O(n) where n is number of digits  
- Space: O(n) for string conversion  

---

## 2. Linked List Cycle (LeetCode 141)

**Problem:**  
Given the head of a linked list, determine if it contains a cycle.

**Approach (Floyd's Cycle-Finding Algorithm):**  
- Initialize two pointers: slow (moves 1 step) and fast (moves 2 steps)  
- Traverse the list:  
  - If fast reaches null → no cycle  
  - If slow meets fast → cycle exists  
- Efficiently detects cycles without extra memory  

**Complexity:**  
- Time: O(n)  
- Space: O(1)  

---
