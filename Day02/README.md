# Coding Challenge Solutions

This repository contains solutions to Day 2 problems.

---

## 1. Middle of the Linked List (LeetCode 876)

**Problem:**  
Given the head of a singly linked list, return the middle node of the linked list.  
If there are two middle nodes, return the second middle node.

**Approach:**  
- Traverse the linked list and store the nodes in a list (array).  
- Calculate the middle index as `len(list) // 2` to get the second middle node if even number of nodes.  
- Return the node at the middle index.  
- Handle the edge case for an empty list by returning `None`.

**Complexity:**  
- Time: O(n), where n is the number of nodes, due to one traversal.  
- Space: O(n), for storing the nodes.

---

## 2. Add Digits (LeetCode 258)

**Problem:**  
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

**Approach:**  
- If `num` is 0, return 0 directly.  
- Otherwise, repeatedly calculate the sum of the digits of `num` until the value is a single digit (less than 10).  
- Convert the number to string to extract digits easily, sum them, and repeat until single digit.  

**Complexity:**  
- Time: O(log n), where n is the size of the input number (number of digits).  
- Space: O(d), where d is the number of digits during summation.

---
