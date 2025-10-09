# Coding Challenge Solutions

Day 36 problems.

---

## 1. Reverse Vowels of a String (LeetCode 345)

**Problem:**  
Given a string, reverse only the vowels in the string and return the result.

**Constraints:**  
- Vowels may appear in both uppercase and lowercase.
- The positions of non-vowel characters should remain unchanged.

**Approach:**  
- Use two pointers (start and end) to scan the string from both sides.
- Swap vowels upon encountering them and move pointers inward.
- Continue until the pointers meet.

**Complexity:**  
- Time: O(n), where n is the length of the string.
- Space: O(n), due to creating a character array.

---

## 2. Sum Root to Leaf Numbers (LeetCode 129)

**Problem:**  
Given the root of a binary tree where every node contains a digit (0-9), each root-to-leaf path represents a number. Return the total sum of all root-to-leaf numbers.

**Constraints:**  
- Binary tree may contain null nodes.
- Each path computes a number by concatenating digits from the root to leaf.

**Approach:**  
- Traverse the tree with a stack or recursion, tracking the current number for each path.
- Add the accumulated number once a leaf node is reached.
- Use either DFS recursion or iterative DFS with a stack.

**Complexity:**  
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(h), where h is the height of the tree if using recursion, or O(n) for stack storage.

---
