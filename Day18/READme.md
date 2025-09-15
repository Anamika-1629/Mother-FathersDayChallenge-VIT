# Coding Challenge Solutions

Day 18 problem.

---

## 1. Implement Queue using Stacks (LeetCode 232)

**Problem:**  
Implement a first in first out (FIFO) queue using only two stacks. The queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

**Constraints:**  
- 1 <= x <= 9 (for push operations)  
- At most 100 operations will be performed  
- All operations are valid (For example, no pop or peek will be called on an empty queue)

**Approach:**  
- Use two stacks (`s1` and `s2`) for queue operations.  
- To `push`, simply append to `s1`.  
- For `pop` and `peek`, move all elements to `s2`, perform the operation from `s2`, then move elements back to `s1`.  
- `empty` checks if `s1` is empty.

**Complexity:**  
- Time: Amortized O(1) per operation  
- Space: O(n), where n is the number of queue elements

---

## 2. Contains Duplicate (LeetCode 217)

**Problem:**  
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

**Constraints:**  
- 1 <= nums.length <= 10^5  
- -10^9 <= nums[i] <= 10^9

**Approach:**  
- Use a set to store seen numbers.  
- Iterate through the array; if a number is already in the set, return `true`.  
- If no duplicates are found, return `false`.

**Complexity:**  
- Time: O(n), where n is the number of elements in `nums`  
- Space: O(n), for the set to store seen numbers

---
