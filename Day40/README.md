# Coding Challenge Solutions

Day 40 problems.

---

## 1. Rotate String

**Problem:**  
Given two strings `s` and `goal`, determine if `s` can become `goal` after some number of shifts, where a shift consists of moving the leftmost character of `s` to the rightmost position.

**Constraints:**  
- Both strings are non-empty and consist of lowercase letters.

**Approach:**  
- If lengths differ, immediately return `False`.
- Concatenate `s` with itself to form `doubled`.
- Check if `goal` is a substring of `doubled`.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(n), for the concatenated string.

---

## 2. Lowest Common Ancestor of a Binary Search Tree

**Problem:**  
Given a binary search tree (BST) and two node values, find their lowest common ancestor (LCA).

**Constraints:**  
- Both nodes exist in the BST.
- The tree is a valid BST.

**Approach:**  
- Traverse the tree recursively or iteratively:
  - If both values are less than the root, move to the left child.
  - If both values are greater, move to the right child.
  - Otherwise, the current node is the LCA.

**Complexity:**  
- Time: O(h), where h is the height of the BST.
- Space: O(h), due to the recursion stack.

---
