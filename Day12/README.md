# Coding Challenge Solutions

Day 12 problems.

---

## 1. Count Odd Numbers in an Interval Range (LeetCode 1523)

**Problem:**  
Given two non-negative integers `low` and `high`, return the count of odd numbers between `low` and `high` (inclusive).

--

**Constraints:**  
- 0 <= low <= high <= 10^9

--

**Approach:**  
- If either `low` or `high` is odd, the odd count is `((high - low) // 2) + 1`.
- Otherwise, it's `(high - low) // 2`.

--

**Complexity:**  
- Time: O(1)
- Space: O(1)

---

## 2. Insert Greatest Common Divisors in Linked List (LeetCode 2807)

**Problem:**  
Given the head of a linked list in which each node contains an integer, insert a new node with the GCD of every pair of adjacent nodes.

--

**Constraints:**  
- The list contains at least 2 nodes.
- Each value is in the range [1, 1000].

--

**Approach:**  
- Traverse the list.
- For every adjacent pair, compute the GCD and insert a new node with that value between them.

--

**Complexity:**  
- Time: O(n log M), where n is number of nodes and M is the maximum node value.
- Space: O(1) additional (modifies list in-place).

---