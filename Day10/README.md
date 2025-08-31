# Coding Challenge Solutions

This repository contains solutions to Day 10 problems.

---

## 1. Delete the Middle Node of a Linked List (LeetCode 2095)

**Problem:**  
You are given the head of a linked list. Delete the middle node, and return the head of the modified list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing.

--

**Constraints:**  
- The number of nodes in the list is in the range [1, 10^5].
- 1 <= Node.val <= 10^5

--

**Approach:**  
- Use two pointers (`fast` and `slow`).  
- Move `fast` at 2x speed and `slow` at 1x speed; keep track of the node before `slow`.
- When `fast` reaches the end, `slow` will be at the middle node.
- Remove the middle node by setting `prev.next = slow.next`.

--

**Complexity:**  
- Time: O(n), where n is the length of the list.
- Space: O(1).

---

## 2. Bulb Switcher (LeetCode 319)

**Problem:**  
There are `n` bulbs that are initially off. You perform a sequence of operations on them as described in the problem. Return the number of bulbs that remain on after n rounds.

--

**Constraints:**  
- 0 <= n <= 10^9

--

**Approach:**  
- Only bulbs at positions that are perfect squares remain on after all operations.
- The answer is the integer part of `sqrt(n)`.

--

**Complexity:**  
- Time: O(1)
- Space: O(1)

---