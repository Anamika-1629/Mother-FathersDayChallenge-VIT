# Coding Challenge Solutions

Day 32 problems.

---

## 1. Binary Tree Level Order Traversal (LeetCode 102)

**Problem:**  
Given the root of a binary tree, return the level order traversal of its nodes’ values (from left to right, level by level).

**Constraints:**  
- Tree nodes may be null.
- Level order traversal groups nodes by level in nested lists.

**Approach:**  
- Use a queue for breadth-first traversal.
- For each level, store node values in a list and enqueue children for the next level.
- Repeat the process until all levels are traversed.

**Complexity:**  
- Time: O(n), where n is the number of nodes.
- Space: O(n), for the queue and result list.

---

## 2. Rotate Image (LeetCode 48)

**Problem:**  
Given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise) in-place.

**Constraints:**  
- You must modify the input matrix directly.
- Do not allocate another 2D matrix for the rotation.

**Approach:**  
- Transpose the matrix (swap rows and columns).
- Reverse each row to complete the 90-degree rotation.
- Everything is done in-place.

**Complexity:**  
- Time: O(n^2), where n is the matrix dimension.
- Space: O(1), as the operations are in-place.

---