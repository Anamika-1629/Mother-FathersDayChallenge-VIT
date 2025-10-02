# Coding Challenge Solutions

Day 30 problems.

---

## 1. Find the Duplicate Number (LeetCode 287)

**Problem:**  
Given an array of integers `nums` containing n + 1 integers where each integer is in the range [1, n] inclusive, find the one repeated number.

**Constraints:**  
- Exactly one repeated number exists in `nums`.  
- You must solve the problem without modifying the array and using only constant extra space.

**Approach:**  
- Use Floyd’s Tortoise and Hare cycle detection algorithm.  
- Initialize two pointers that iterate through the array at different speeds.  
- Detect the cycle (duplicate) and find its entry point which is the duplicate number.

**Complexity:**  
- Time: O(n).  
- Space: O(1).

---

## 2. Diameter of Binary Tree (LeetCode 543)

**Problem:**  
Given the root of a binary tree, return the length of the diameter of the tree.

**Constraints:**  
- The diameter is the length of the longest path between any two nodes in a tree.  
- The path may or may not pass through the root.  
- Length is measured as the number of edges between nodes.

**Approach:**  
- Use depth-first search (DFS) to compute the height of left and right subtrees recursively.  
- Maintain the maximum sum of left and right subtree heights during traversal as the diameter.  
- The diameter is the maximum of all such sums encountered.

**Complexity:**  
- Time: O(n).
- Space: O(h) where h is the height of the tree (due to recursion stack).

---