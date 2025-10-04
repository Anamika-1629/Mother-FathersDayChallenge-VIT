# Coding Challenge Solutions

Day 31 problems.

---

## 1. Maximum Depth of Binary Tree (LeetCode 104)

**Problem:**  
Given the root of a binary tree, return its maximum depth.

**Constraints:**  
- A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
- The tree may be empty.

**Approach:**  
- Use recursion to explore each subtree and compute its depth.
- For any node, maximum depth is 1 plus the maximum of the depths of its left and right children.

**Complexity:**  
- Time: O(n), where n is the number of nodes.
- Space: O(h), where h is the height of the tree (due to recursion stack).

---

## 2. Flipping an Image (LeetCode 832)

**Problem:**  
Given an n x n binary matrix `image`, flip the image horizontally, then invert it, and return the resulting image.

**Constraints:**  
- Each row of the image can be flipped and inverted independently.
- Input is a binary matrix.

**Approach:**  
- Iterate over each row.
- Use two-pointer technique to simultaneously reverse the row and invert each element (0 becomes 1, 1 becomes 0).
- Swap and invert values from both ends towards the middle.

**Complexity:**  
- Time: O(n^2), where n is the row or column length.
- Space: O(1), since the operation is in-place.

---