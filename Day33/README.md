# Coding Challenge Solutions

Day 33 problems.

---

## 1. Binary Tree Right Side View (LeetCode 199)

**Problem:**  
Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking at the tree from the right side.

**Constraints:**  
- Nodes can be null.
- The output should be a list of visible node values from the rightmost perspective.

**Approach:**  
- Perform a level order (BFS) traversal using a queue.
- For each level, add the last node’s value to the result.
- Enqueue the left and right children to process subsequent levels.

**Complexity:**  
- Time: O(n), where n is the number of nodes.
- Space: O(n), for the queue and result list.

---

## 2. Lexicographically Smallest Palindrome (LeetCode 2697)

**Problem:**  
Given a string consisting of lowercase English letters, you are allowed to replace characters to make the string a palindrome with the minimum number of operations. If multiple such palindromes are possible, return the lexicographically smallest one.

**Constraints:**  
- The input is a non-empty string of lowercase English letters.
- Each replacement must yield a valid palindrome.

**Approach:**  
- Use two pointers from both ends of the string.
- For each pair of characters, replace the larger character with the smaller to minimize lexicographical order.
- Continue until all pairs are checked or overlap.

**Complexity:**  
- Time: O(n), where n is the string length.
- Space: O(n), for the character array.

---
