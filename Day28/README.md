# Coding Challenge Solutions

Day 28 problems.

---

## 1. Maximum Subarray (LeetCode 53)

**Problem:**  
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

**Constraints:**  
- Array may include negative and positive integers.  
- Subarray must be contiguous.

**Approach:**  
- Use Kadane’s algorithm: maintain the maximum sum ending at each position.  
- For each index, update current sum as `max(current_element, current_sum + current_element)`.  
- Track maximal sum seen so far.

**Complexity:**  
- Time: O(n), where n is the length of the array.  
- Space: O(1)

---

## 2. Path Sum (LeetCode 112)

**Problem:**  
Given the root of a binary tree and an integer `targetSum`, return true if the tree has a root-to-leaf path with values adding up to `targetSum`.

**Constraints:**  
- Tree nodes may be null.  
- Only root-to-leaf paths considered.

**Approach:**  
- Use recursion to traverse tree.  
- At each node, subtract node value from `targetSum` and go deeper.  
- If a leaf matches remaining sum, return true.

**Complexity:**  
- Time: O(n), with n as number of nodes.  
- Space: O(h), where h is the tree height (recursion stack).

---