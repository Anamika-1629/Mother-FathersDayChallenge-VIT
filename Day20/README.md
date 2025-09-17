# Coding Challenge Solutions

Day 20 problem.

---

## 1. Evaluate Reverse Polish Notation (LeetCode 150)

**Problem:**  
Given an array of strings `tokens` that represents an arithmetic expression in Reverse Polish Notation, evaluate the expression and return an integer result representing its value.

**Constraints:**  
- `1 <= tokens.length <= 10^4`  
- `tokens[i]` is either an integer or one of `"+", "-", "*", "/"`  
- Division between two integers should truncate toward zero.  
- The input is always valid Reverse Polish Notation.

**Approach:**  
- Use a stack to evaluate the expression:
  - For each token, if it is a number, push it onto the stack.
  - If it's an operator, pop the last two numbers from the stack, apply the operation, and push the result back onto the stack.
- The final result will be the only remaining value in the stack.

**Complexity:**  
- Time: O(n), as each token is processed once.  
- Space: O(n), to store numbers in the stack for intermediate operations.

---

## 2. Find Greatest Common Divisor of Array (LeetCode 1979)

**Problem:**  
Given an integer array `nums`, return the greatest common divisor (GCD) of the smallest and largest integers in the array. The GCD of two numbers is the largest positive integer that divides both.

**Constraints:**  
- `2 <= nums.length <= 1000`  
- `1 <= nums[i] <= 1000`

**Approach:**  
- Find the minimum and maximum elements in the array.
- Iterate from `min` downward, checking for the highest integer that divides both `min` and `max` without a remainder.
- Return this integer as the GCD.

**Complexity:**  
- Time: O(n + min), iterating through the list to find min/max, and then another loop from min to 1 for the GCD calculation.
- Space: O(1), using a fixed number of variables for computation.

---
