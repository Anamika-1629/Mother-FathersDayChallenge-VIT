# Coding Challenge Solutions

Day 24 problems.

---

## 1. Basic Calculator (LeetCode 224)

**Problem:**  
Given a string representing a valid expression, implement a basic calculator to evaluate it and return the result of the evaluation.

**Constraints:**  
- The input string may contain digits, '+', '-', '(', ')', and spaces.
- All expressions are valid; input contains only valid characters.
- No use of built-in eval() or similar functions.

**Approach:**  
- Iterate through the expression character by character.  
- Use a stack to keep track of results and signs when encountering parentheses.  
- Accumulate multi-digit numbers and apply the appropriate sign.  
- On seeing '(', push the current result and sign to the stack and reset the result for new scope.  
- On seeing ')', resolve the current scope using the stack.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---

## 2. Move Zeroes (LeetCode 283)

**Problem:**  
Given an integer array nums, move all 0's to the end while maintaining the relative order of the non-zero elements.

**Constraints:**  
- Modify nums in-place (do not create a copy).
- Try to minimize the number of operations.

**Approach:**  
- Use a loop to iterate over nums.  
- When a zero is found, remove it and append a zero to the end; keep track of how many zeros are moved.  
- Continue looping until all non-zero elements have been processed in place.

**Complexity:**  
- Time: O(n^2) for the pop/append approach (as shown), or O(n) for the optimal two-pointer method.  
- Space: O(1)

---