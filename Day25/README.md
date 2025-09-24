# Coding Challenge Solutions

Day 25 problems.

---

## 1. Rotate Array (LeetCode 189)

**Problem:**  
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

**Constraints:**  
- k may be larger than the length of nums.  
- Modify the input array in-place without returning anything.

**Approach:**  
- Compute k = k % n to handle large k values.  
- Reverse the entire array.  
- Reverse the first k elements.  
- Reverse the remaining elements.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---

## 2. Implement Stack using Queues (LeetCode 225)

**Problem:**  
Implement a last-in-first-out (LIFO) stack using only two queues and support typical stack operations: push, pop, top, and empty.

**Constraints:**  
- Utilize only two internal queues to simulate stack behavior.

**Approach:**  
- Push element in to the empty queue q2.  
- Transfer all elements from q1 to q2.  
- Swap q1 and q2 references to keep the newest element at front.  
- Pop elements from q1 for the stack pop operation; top is the head of q1.

**Complexity:**  
- Time: O(n) per push  
- Space: O(n)

---