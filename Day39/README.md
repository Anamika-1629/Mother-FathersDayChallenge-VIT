# Coding Challenge Solutions

Day 39 problems.

---

## 1. Remove All Adjacent Duplicates in String

**Problem:**  
Given a string of lowercase English letters, repeatedly remove pairs of adjacent duplicate letters until none remain. Return the resulting string.

**Constraints:**  
- The input consists only of lowercase letters.
- Removal should continue as long as adjacent duplicates remain.

**Approach:**  
- Use a stack to track characters.
- For each character, check if it matches the top of the stack.
- If it does, pop the stack (remove duplicate pair); otherwise, push the character.
- Finally, join the stack contents to get the result string.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(n), for stack storage.

---

## 2. Insert into a Binary Search Tree

**Problem:**  
Given the root of a Binary Search Tree (BST) and a value to insert, return the root node of the tree after the insertion. The value is guaranteed not to exist in the original BST.

**Constraints:**  
- The tree must remain a valid BST after insertion.
- The input BST may contain any number of nodes and may be empty.

**Approach:**  
- Recursively traverse the tree to locate the correct position for the new value.
- Insert the new node as a leaf at that position.
- Return the updated root node.
- For output, display the BST's in-order traversal.

**Complexity:**  
- Time: O(h), where h is the height of the tree.
- Space: O(h), due to recursion stack or explicit stack for iterative implementations.

---
