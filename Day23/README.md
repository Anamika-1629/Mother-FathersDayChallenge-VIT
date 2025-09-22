# Coding Challenge Solutions

Day 23 problems.

---

## 1. Longest Valid Parentheses (LeetCode 32)

**Problem:**  
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

**Constraints:**  
- The input string consists of only '(' and ')'.

**Approach:**  
- Use a stack to keep track of the indices of characters.  
- Initialize the stack with -1 to handle edge cases.  
- Iterate through the string:  
  - If '(' encountered, push its index onto the stack.  
  - If ')' encountered, pop the top of the stack.  
    - If the stack becomes empty, push the current index (to reset the base).  
    - Else, update max length with the difference between current index and stack's top.  

**Complexity:**  
- Time: O(n)  
- Space: O(n)  

---

## 2. Search Insert Position (LeetCode 35)

**Problem:**  
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

**Constraints:**  
- The array is sorted and contains distinct integers.

**Approach:**  
- Use binary search to find the target's position or insertion point.  
- Initialize low and high pointers.  
- While low <= high, check mid element:  
  - If equal to target, return mid index.  
  - If less than target, move low to mid + 1.  
  - Else, move high to mid - 1.  
- Return low as the insert position after the search completes.

**Complexity:**  
- Time: O(log n)  
- Space: O(1)  

---
