# Coding Challenge Solutions

Day 34 problems.

***

## 1. Flatten Binary Tree to Linked List (LeetCode 114)

**Problem:**  
Given the root of a binary tree, flatten the tree into a "linked list" where each right child points to the next node in preorder traversal, and all left pointers become null.

**Constraints:**  
- The binary tree may contain null nodes.
- The result should maintain the original node values and order per preorder traversal.

**Approach:**  
- Use an iterative strategy starting from the root.
- For each node with a left child, find its rightmost node and attach the original right subtree.
- Move the left subtree to the right and set the left child to null.
- Repeat for every node proceeding along the right chain.

**Complexity:**  
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(1), all operations are in-place and only pointers are used.

***

## 2. Length of Last Word (LeetCode 58)

**Problem:**  
Given a string consisting of words and spaces, return the length of the last word in the string.

**Constraints:**  
- The input string may contain leading or trailing spaces.
- Words are separated by spaces and consist of contiguous non-space characters.

**Approach:**  
- Start from the end of the string and skip trailing spaces.
- Count the length of the last word by iterating backwards until a space is encountered or the string begins.
- Return the final count.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(1), as only a few extra variables are used.

---