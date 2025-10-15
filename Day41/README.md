# Coding Challenge Solutions

Day 41 problems.

---

## 1. Delete Node in a Binary Search Tree (BST)

**Problem:**  
Given the root of a BST and a key, delete the node with the given key in the BST and return the updated root.

**Constraints:**  
- The BST property must be maintained after deletion.
- Deletion involves either removing a leaf, replacing with child, or replacing with in-order successor.
- Tree nodes may contain nulls.

**Approach:**  
- Recursively traverse tree to find node with key.
- When found:  
  - If node has no children or one child, replace with child or null.  
  - If node has two children, replace with in-order successor (minimum in right subtree) and delete successor node.
- Return updated root.

**Complexity:**  
- Time: O(h), where h = height of BST.
- Space: O(h), due to recursion stack.

---

## 2. Longest Common Prefix

**Problem:**  
Given an array of strings, find the longest common prefix among them. If no common prefix exists, return an empty string.

**Constraints:**  
- Input array may be empty.
- Strings contain lowercase and uppercase letters.

**Approach:**  
- Initialize prefix as the first string.
- For each next string, shrink prefix from the end until it matches the start of the string.
- If prefix becomes empty, return empty string immediately.
- Return the final prefix.

**Complexity:**  
- Time: O(S), where S is the sum of all characters in all strings.
- Space: O(1), in-place prefix shrinking.

---
