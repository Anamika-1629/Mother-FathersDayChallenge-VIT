# Coding Challenge Solutions

Day 1 problems.

---

## 1. Missing Number (LeetCode 268)

**Problem:**  
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

**Approach:**  
- Calculate the expected sum of numbers from `0` to `n` using the formula n × (n + 1) / 2.  
- Compute the actual sum of elements in `nums`.  
- The missing number is the difference between the expected sum and the actual sum.  
- This works because the array is guaranteed to contain all numbers except one missing number.

**Complexity:**  
- Time: O(n), single pass to sum elements.  
- Space: O(1), constant extra space.  

---

## 2. Reverse Linked List (LeetCode 206)

**Problem:**  
Given the head of a singly linked list, reverse the list and return the reversed list.

**Approach:**  
- Initialize two pointers: `prev` as `None` and `current` as `head`.  
- Traverse the linked list:  
  - Store the next node temporarily.  
  - Reverse the `next` pointer of the current node to point to `prev`.  
  - Move `prev` and `current` one step forward.  
- At the end, `prev` points to the new head of the reversed list.  
- Return `prev`.

**Complexity:**  
- Time: O(n), traversing the list once.  
- Space: O(1), reversing pointers in place.  

---