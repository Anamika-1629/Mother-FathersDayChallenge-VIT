# Coding Challenge Solutions

Day 22 problems.

---

## 1. Majority Element (LeetCode 169)

**Problem:**  
Given an array nums of size n, return the majority element.  
The majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.

**Constraints:**  
- 1 <= nums.length <= 5 * 10^4  
- The majority element always exists.

**Approach:**  
- Use Boyer-Moore Voting Algorithm.  
- Initialize candidate and count = 0.  
- Iterate over array, if count is zero, set candidate to current num.  
- Increment count if current num == candidate, else decrement.  
- Return candidate at the end.

**Complexity:**  
- Time: O(n)  
- Space: O(1)

---

## 2. Minimum Remove to Make Valid Parentheses (LeetCode 1249)

**Problem:**  
Given a string s of '(', ')' and lowercase English characters, remove the minimum number of parentheses so that the resulting string is valid and return any valid string.

**Constraints:**  
- 1 <= s.length <= 10^5  
- s consists of '(' , ')' and lowercase English letters.

**Approach:**  
- Use a stack to track indices of unmatched '('.  
- Iterate string, mark invalid ')' or set to empty.  
- Remove remaining '(' indices after traversal.  
- Join remaining characters for final string.

**Complexity:**  
- Time: O(n)  
- Space: O(n)

---
