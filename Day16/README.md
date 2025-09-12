# Coding Challenge Solutions

Day 16 problem.

---

## 1. Sum of Square Numbers (LeetCode 633)

**Problem:**  
Given a non-negative integer `c`, decide whether there exist two integers `a` and `b` such that a^2 + b^2 = c. 

---

**Constraints:**  
- 0 <= c <= 2^31 - 1

---

**Approach:**  
- Loop `a` from 0 to sqrt(c).
- For each `a`, compute `b_sq = c - a*a`.
- Let `b = int(b_sq ** 0.5)`.
- Return `True` if `b * b == b_sq` for any `a`.
- Return `False` if no such pair is found.

---

**Complexity:**  
- Time: O(sqrt(c))
- Space: O(1)

---

## 2. Delete Node in a Linked List (LeetCode 237)

**Problem:**  
Given only access to a node (not the head) in a singly-linked list, delete that node in-place so the list no longer contains it.

---

**Constraints:**  
- The given node is not the tail and is always valid.
- No access to the head of the list.

---

**Approach:**  
- Copy the value from the next node into the current node.
- Update the current node's next pointer to skip the next node, effectively removing it.

---

**Complexity:**  
- Time: O(1)
- Space: O(1)

---