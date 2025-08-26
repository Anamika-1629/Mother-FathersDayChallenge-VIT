# Coding Challenge Solutions

This repository contains solutions to Day 5 problems.

---

## 1. Valid Perfect Square (LeetCode 367)

**Problem:**  
Given a positive integer `num`, return `true` if `num` is a perfect square, and `false` otherwise.  
A perfect square is an integer that is the square of some integer.  
**Note:** You must not use any built-in library function, such as `sqrt`.

**Approach (Binary Search):**  
- Perform binary search in the range [1, num].  
- Check if the middle value squared equals `num`.  
- Adjust the search boundaries accordingly.  
- If found, return true; if the loop ends, return false.  

**Complexity:**  
- Time: O(log n), where n = `num` (binary search iterations).  
- Space: O(1).  

---

## 2. Palindrome Linked List (LeetCode 234)

**Problem:**  
Given the head of a singly linked list, return `true` if it is a palindrome, otherwise `false`.

**Approach (Two-Pointer + Reverse Second Half):**  
- Use two pointers (`slow` and `fast`) to find the middle of the list.  
- Reverse the second half of the list in place.  
- Compare the first half with the reversed second half, node by node.  
- Return `true` if all values match, otherwise `false`.  

**Complexity:**  
- Time: O(n), where n is the number of nodes.  
- Space: O(1), since the reversal is done in place.  

---
