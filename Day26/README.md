# Coding Challenge Solutions

Day 26 problems.

---

## 1. Binary Tree Inorder Traversal (LeetCode 94)

**Problem:**  
Given the root of a binary tree, return the inorder traversal of its nodes' values.

**Constraints:**  
- Handle null nodes gracefully.  
- Return the traversal as a list of integers.

**Approach:**  
- Use a stack for iterative inorder traversal.  
- Traverse left subtree first, then node, then right subtree.  
- Alternatively, use recursion to visit left, root, and right.

**Complexity:**  
- Time: O(n), where n is the number of nodes.  
- Space: O(n) for stack or recursion call stack.

---

## 2. Find First and Last Position of Element in Sorted Array (LeetCode 34)

**Problem:**  
Given a sorted array of integers (non-decreasing order), find the starting and ending position of a given target value. Return [-1, -1] if not found.

**Constraints:**  
- Must achieve O(log n) runtime complexity using binary search.

**Approach:**  
- Use two binary searches to find the first and last occurrences separately.  
- Narrow search space by adjusting left and right pointers based on target comparison.

**Complexity:**  
- Time: O(log n)  
- Space: O(1)

---