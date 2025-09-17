# Coding Challenge Solutions

Day 21 problem.

---

## 1. Valid Parenthesis String (LeetCode 678)

**Problem:**  
Given a string `s` containing only three types of characters: `'('`, `')'`, and `'*'`, return `True` if the string is valid.  
A valid string obeys these rules:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- The character `'*'` can be treated as `'('`, `')'`, or an empty string.

**Constraints:**  
- `1 <= s.length <= 100`  
- `s[i]` is `'('`, `')'` or `'*'`

**Approach:**  
- Use two counters, `low` and `high`, to track the possible range of open parentheses.
- For each character:
  - If `'('`, increment both `low` and `high`.
  - If `')'`, decrement both.
  - If `'*'`, decrement `low` and increment `high`.
- If at any point `high` becomes negative, the string is invalid.
- If `low` drops below zero, reset it to zero since we cannot have negative open parentheses.
- The string is valid if `low` is zero at the end.

**Complexity:**  
- Time: O(n), as every character is processed once.
- Space: O(1), just using counters.

---

## 2. Pascal's Triangle II (LeetCode 119)

**Problem:**  
Given an integer `rowIndex`, return the rowIndex-th (0-indexed) row of the Pascal's triangle.  
In Pascal's triangle, each number is the sum of the two numbers directly above it.

**Constraints:**  
- `0 <= rowIndex <= 33`

**Approach:**  
- Create a list of length `rowIndex+1` initialized with `1`.
- Iterate from 2 to `rowIndex`, updating the row from right to left by adding the previous values.
- This approach efficiently generates the required row without constructing the entire triangle.

**Complexity:**  
- Time: O(n^2), as there are two nested loops iterating up to `rowIndex`.
- Space: O(n), the result row list.

---
