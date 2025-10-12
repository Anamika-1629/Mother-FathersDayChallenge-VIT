# Coding Challenge Solutions

Day 38 problems.

---

## 1. Valid Palindrome

**Problem:**  
Given a string, check if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

**Constraints:**  
- A phrase is a palindrome if, after conversion, it reads the same forward and backward.
- Only alphanumeric characters (letters and numbers) are considered.
- Input may contain spaces and punctuation.

**Approach:**  
- Use two pointers, starting at each end of the string.
- Skip characters that are not alphanumeric.
- Compare lowercase forms of characters at both pointers.
- Continue until pointers cross; return `true` if all comparisons pass, otherwise `false`.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(1), checks performed in-place (excluding input storage).

---

## 2. Search in a Binary Search Tree

**Problem:**  
Given the root of a binary search tree and an integer `val`, return the subtree rooted with node having value `val`. If such a node does not exist, return `null`.

**Constraints:**  
- The input tree is a valid BST and may contain null nodes.
- If a subtree with the target value is found, output the values in in-order traversal.

**Approach:**  
- Start at the root and traverse recursively.
- If `val` matches the current node's value, return that node.
- If `val` is less, search the left subtree; if more, search the right subtree.
- If no matching node is found, return `null`.

**Complexity:**  
- Time: O(h), where h is the height of the tree.
- Space: O(h), due to recursion stack (worst case O(n) if the tree is unbalanced).

---
