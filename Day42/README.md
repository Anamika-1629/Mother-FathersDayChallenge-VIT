# Coding Challenge Solutions

Day 42 problems.

---

## 1. Validate Binary Search Tree (BST)

**Problem:**  
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

**Constraints:**  
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
- Node values may repeat or be null in the input representation.

**Approach:**  
- Perform an in-order traversal (iterative using a stack) and check whether all node values appear in strictly increasing order.
- Keep track of the previously visited node's value and compare each node with it during traversal.
- Return False immediately if any current value is not greater than the previous value.

**Complexity:**  
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(h), where h is the height of the tree due to the stack used for traversal.

---

## 2. Reverse Words in a String

**Problem:**  
Given an input string, reverse the order of the words.

**Constraints:**  
- Input string may contain leading or trailing spaces.
- Words are always separated by at least one space.
- No leading or trailing spaces in the output, and words are separated by a single space.

**Approach:**  
- Split the string by whitespace to extract words.
- Reverse the list of words.
- Join the words using a single space to create the final string.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(n), for storing the list of words and the output string.

---