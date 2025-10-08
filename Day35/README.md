# Coding Challenge Solutions

Day 35 problems.

---

## 1. Lowest Common Ancestor of a Binary Tree (LeetCode 236)

**Problem:**  
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

**Constraints:**  
- The binary tree may contain null nodes.
- Nodes $$p$$ and $$q$$ are guaranteed to be present in the tree.

**Approach:**  
- Use recursion to explore left and right subtrees.
- If the root matches either $$p$$ or $$q$$ or is null, return root.
- Recurse on left and right children; if both return non-null, root is the LCA.
- Otherwise, propagate the non-null result upwards.

**Complexity:**  
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(n), for recursive stack in the worst case.

---

## 2. Number of Segments in a String (LeetCode 434)

**Problem:**  
Given a string, return the number of segments in the string (a segment is a sequence of non-space characters).

**Constraints:**  
- Input may contain leading, trailing, or multiple spaces between words.
- Only contiguous non-space sequences count as segments.

**Approach:**  
- Split the string by spaces and count non-empty entries.
- Alternatively, iterate through the string and count transitions from space to non-space.

**Complexity:**  
- Time: O(n), where n is the length of the input string.
- Space: O(n), if split is used; O(1) for pointer traversal.

---