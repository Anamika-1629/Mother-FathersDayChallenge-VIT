# Coding Challenge Solutions

Day 17 problem.

---

## 1. Two Sum (LeetCode 1)

**Problem:**  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  
Assume each input has exactly one solution, and do not use the same element twice.

**Constraints:**  
- 2 <= nums.length <= 10^4  
- -10^9 <= nums[i] <= 10^9  
- -10^9 <= target <= 10^9  
- Exactly one solution exists.

**Approach:**  
- Use a brute-force double loop over all pairs `(i, j)` where $$ i < j $$.
- For each pair, check if `nums[i] + nums[j] == target`.
- If so, return their indices immediately.
- Accept array size, elements, and target from user input using `Scanner`.
- Print indices on success.

**Complexity:**  
- Time: $$ O(n^2) $$, where $$ n $$ is the length of `nums`.
- Space: $$ O(1) $$, aside from the result array.

---

## 2. Min Stack (LeetCode 155)

**Problem:**  
Design a stack supporting push, pop, top, and retrieving the minimum element in constant time.

**Constraints:**  
- Operations must run in constant time.
- Can be implemented with extra space.

**Approach:**  
- Maintain two stacks: `stack` for all values, and `min_stack` for tracking the current minimum.
- On each push, append value and update `min_stack` if new value is <= current minimum.
- On pop, remove value, and pop `min_stack` if popped value was the minimum.
- Support `top` and `getMin` methods.
- Accept a sequence of commands (`push`, `pop`, `top`, `getMin`) from user input.

**Complexity:**  
- Time: $$ O(1) $$ per operation.
- Space: $$ O(n) $$ for stack size $$ n $$.

---