# Coding Challenge Solutions

Day 14 problem.

---

## 1. Sign of the Product of an Array (LeetCode 1822)

**Problem:**   
Given an integer array, determine the sign of the product of all elements:   
- Return `1` if the product is positive   
- Return `-1` if negative   
- Return `0` if the product contains zero   

**Constraints:**   
- Elements can be any integers, including zero and negatives.

**Approach:**   
- Initialize a sign variable as `1`.   
- Iterate over the array:   
  - If an element is `0`, return `0` immediately.   
  - If an element is negative, flip the sign by multiplying by `-1`.   
- After full traversal, return the final sign.

**Complexity:**   
- Time: O(n), where n is the length of the array   
- Space: O(1)

---

## 2. Remove Duplicates from Sorted List II (LeetCode 82)

**Problem:**   
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

**Constraints:**   
- The linked list is sorted.   
- Can contain duplicate values.   

**Approach:**   
- Use a dummy node pointing to the head for easier edge case handling.   
- Maintain a pointer `prev` and traverse with a `head` pointer.   
- For a sequence of duplicates, skip all nodes with that value and connect `prev.next` to the first distinct node after duplicates.   
- Otherwise, move `prev` forward.

**Complexity:**   
- Time: O(n), where n is number of nodes in the list   
- Space: O(1), in-place modification

---