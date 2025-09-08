# Coding Challenge Solutions

Day 9 problems.

---

## 1. Nth Digit (LeetCode 400)

**Problem:**  
Given an integer `n`, return the `n`th digit of the infinite integer sequence `[1, 2, 3, 4, 5, 6, ...]`.

--

**Constraints:**  
- 1 <= n <= 2<sup>31</sup> - 1

--

**Approach:**  
- Determine the length `l` of numbers (`1` for 1-9, `2` for 10-99, etc.) where the nth digit falls.
- Remove all digits belonging to smaller-length groups (reduce `n`).
- Calculate the exact starting number and index of the required digit.
- Convert the number to string and index the desired digit.

--

**Complexity:**  
- Time: O(log n)
- Space: O(1)

---

## 2. Swapping Nodes in a Linked List (LeetCode 1721)

**Problem:**  
You are given the head of a linked list and an integer `k`.  
Swap the values of the `k`th node from the start and the `k`th node from the end (list is 1-indexed).

--

**Constraints:**  
- The number of nodes in the list is in the range [1, 10<sup>5</sup>]
- 0 <= Node.val <= 100  
- 1 <= k <= length of the list

--

**Approach:**  
- Traverse to the kth node from the start and store it.
- Traverse to the kth node from the end using two pointers (the first pointer goes `k` steps ahead, then move both together until the first hits end).
- Swap the values of the two nodes.

--

**Complexity:**  
- Time: O(n), where n is the number of nodes.
- Space: O(1)

--