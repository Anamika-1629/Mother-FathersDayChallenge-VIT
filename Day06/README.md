# Coding Challenge Solutions

This repository contains solutions to Day 6 problems.

---

## 1. Valid Perfect Square (LeetCode 367)

**Problem:**  
Given a positive integer `num`, return `true` if `num` is a perfect square, and `false` otherwise.  
A perfect square is an integer that is the square of an integer (the product of some integer with itself).  
You must not use any built-in library function, such as `sqrt`.

**Approach:**  
- Use binary search between 1 and `num` to find the integer whose square matches `num`.  
- Calculate the midpoint and square it to compare with `num`.  
- Narrow search space until the exact square root is found or the search space is fully checked.  
- Return `true` if the square equals `num`, otherwise `false`.  

**Complexity:**  
- Time: O(log n), where n = `num` (due to binary search).  
- Space: O(1).

---

## 2. Palindrome Linked List (LeetCode 234)

**Problem:**  
Given the head of a singly linked list, return `true` if it is a palindrome, and `false` otherwise.

**Approach:**  
- Use two pointers (`slow` and `fast`) to find the middle of the linked list.  
- Reverse the second half of the list.  
- Compare node values of the first half and the reversed second half.  
- Return `true` if all corresponding nodes match, otherwise `false`.  

**Complexity:**  
- Time: O(n), where n is the number of nodes in the list.  
- Space: O(1), as the reversal is done in place without extra memory.

---
