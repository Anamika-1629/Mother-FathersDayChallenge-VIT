# Coding Challenge Solutions

Day 43 problems.

---

## 1. Zigzag Conversion

**Problem:**  
Given a string and a number of rows, write the string in a zigzag pattern on the given number of rows, then read line by line.

Example:  
Input: "PAYPALISHIRING", rows=3  
Output: "PAHNAPLSIIGYIR"

**Constraints:**  
- If the number of rows is 1 or greater than or equal to the string length, return the original string.
- The string contains only uppercase and lowercase letters.

**Approach:**  
- Use an array of StringBuilders, one for each row.
- Iterate through characters, appending to the current row.
- Change direction when you reach the top or bottom row.
- Join all rows to build the final result.

**Complexity:**  
- Time: O(n), where n is the length of the string.  
- Space: O(n), for the storage of characters in rows.

---

## 2. Kth Smallest Element in a BST

**Problem:**  
Given the root of a binary search tree and an integer k, return the kth smallest element (1-indexed) of all the values in the tree.

**Constraints:**  
- The BST contains unique integer values.
- 1 ≤ k ≤ number of nodes in the tree.

**Approach:**  
- Use iterative in-order traversal with a stack.
- Traverse left subtree until no more nodes.
- Pop nodes from stack and decrement k.
- When k reaches 0, return the current node's value.
- Continue traversal on right subtree as needed.

**Complexity:**  
- Time: O(h + k), where h is the height of the tree.  
- Space: O(h), due to recursion stack or iterative stack usage.

---