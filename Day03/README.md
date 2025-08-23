# Coding Challenge Solutions

This repository contains solutions to Day 3 problems.

---

## 1. Perfect Number (LeetCode 507)

**Problem:**  
A perfect number is a positive integer that equals the sum of its proper positive divisors (excluding itself). Given an integer `num`, return `true` if it's perfect, otherwise `false`.

**Approach:**  
- Handle edge cases (numbers ≤ 1) immediately  
- Initialize sum with 1 (smallest proper divisor)  
- Check divisors only up to √num for efficiency  
- For each divisor found:  
  - Add both the divisor and its complement  
  - Avoid duplicate addition for square numbers  
  - Early termination if sum exceeds num  
- Compare final sum to original number  

**Complexity:**  
- Time: O(√n)  
- Space: O(1)  

---

## 2. Merge Two Sorted Lists (LeetCode 21)

**Problem:**  
Merge two sorted linked lists and return the head of the merged list.

**Approach:**  
- Create dummy node as starting point  
- Use current pointer to build new list  
- Compare nodes from both lists:  
  - Attach smaller node to current  
  - Move pointer of the list that contributed the node  
- Attach remaining nodes when one list is exhausted  

**Complexity:**  
- Time: O(n + m)  
- Space: O(1)  

---
