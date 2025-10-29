# Coding Challenge Solutions

Day 50 problems.

---

## 1. Break a Palindrome

**Problem:**  
Given a palindromic string of lowercase English letters, replace exactly one character with any lowercase English letter so the resulting string is not a palindrome and is the lexicographically smallest possible.  
Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

**Constraints:**  
- 1 ≤ palindrome.length ≤ 1000  
- palindrome consists only of lowercase English letters.

**Approach:**  
- If the length is 1, return an empty string since any single character is always a palindrome.
- Iterate through the first half of the string. If a non-'a' character is found, replace it with 'a' and return the result immediately (minimizing lexicographic order).
- If all characters in the first half are 'a', change the last character to 'b'.

**Complexity:**  
- Time: O(n), where n is the length of the string (you may check up to n/2 characters).
- Space: O(n), for constructing the mutable version of the string.

---