# Coding Challenge Solutions

Day 29 problems.

---

## 1. Kth Largest Element in an Array (LeetCode 215)

**Problem:**  
Given an integer array `nums` and an integer `k`, return the kth largest element in the array.

**Constraints:**  
- The kth largest element means the kth element in sorted order, not the kth distinct element.  
- Array may include duplicates, negative and positive integers.

**Approach:**  
- Use a min-heap (priority queue) of size k to store the largest k elements while traversing the array.  
- Add each element to the heap and remove the smallest if the heap size exceeds k.  
- The root of the min-heap is the kth largest element.

**Complexity:**  
- Time: O(n log k), where n is the length of the array.  
- Space: O(k)

---

## 2. Sum of Left Leaves (LeetCode 404)

**Problem:**  
Given the root of a binary tree, return the sum of all left leaves.

**Constraints:**  
- Tree nodes may be null.  
- Only leaves that are left children of their parent are considered.

**Approach:**  
- Use recursion to traverse the binary tree.  
- At each node, check if the left child is a leaf, and add its value if so.  
- Recursively accumulate the sum from left and right subtrees.

**Complexity:**  
- Time: O(n), where n is the number of nodes.  
- Space: O(h), where h is the height of the tree (recursion stack).

---