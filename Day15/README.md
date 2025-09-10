# Coding Challenge Solutions

Day 15 problem.

---

## 1. Excel Sheet Column Title (LeetCode 168)

**Problem:**  
Given an integer `columnNumber`, return its corresponding column title as it appears in an Excel sheet (e.g., 1 → "A", 28 → "AB", 701 → "ZY")[attached_image:1][attached_image:2].

--

**Constraints:**  
- \(1 \leq\) columnNumber \(\leq 2^{31} - 1\)

--

**Approach:**  
- Treat the conversion as mapping to a 26-letter alphabet (like base-26) but without a zero: 'A' is 1, ..., 'Z' is 26.
- While the number is positive:
  - Subtract 1 (to make it zero-based),
  - Compute `columnNumber % 26` to find the letter,
  - Prepend corresponding letter,
  - Divide columnNumber by 26.
- Repeat until the number becomes zero.

--

**Complexity:**  
- Time: O(\(\log_{26}n\)), where n is the column number  
- Space: O(1), ignoring output string

---

## 2. Add Two Numbers (LeetCode 2)

**Problem:**  
You are given two non-empty linked lists representing two non-negative integers, with digits stored in reverse order (each node contains a single digit). Add the two numbers and return the sum as a linked list[attached_image:3].

--

**Constraints:**  
- Both input lists are non-empty and represent non-negative integers
- Digits are stored in reverse order (least significant digit first)
- Each node contains a single digit (0-9)
- Input lists may have different lengths

--

**Approach:**  
- Use a dummy head node to simplify list construction.
- Traverse both input lists simultaneously, digit by digit:
  - Compute sum of the current nodes' values and carry.
  - Update carry and add a new node with the digit part.
  - Handle remaining carry after loop.
- Result list represents the sum in the same reverse order.

--

**Complexity:**  
- Time: O(\( \max(m, n) \)), where m and n are lengths of the input lists  
- Space: O(\( \max(m, n) \)), for the output list

---
