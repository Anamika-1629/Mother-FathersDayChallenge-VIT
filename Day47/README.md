# Coding Challenge Solutions

Day 47 problems.

---

## 1. Number of Substrings Containing All Three Characters

**Problem:**  
Given a string `s` consisting only of characters 'a', 'b', and 'c', return the number of substrings containing at least one occurrence of all three characters.

**Constraints:**  
- 1 ≤ s.length ≤ 5 × 10^4  
- `s` consists only of 'a', 'b', and 'c'.

**Approach:**  
- Track the latest index for each character as you iterate.  
- For every position, if all three have appeared, the smallest of their indices gives possible starting positions for substrings ending at the current index.  
- Add that count to the answer.

**Complexity:**  
- Time: O(n), where n is the length of the string.  
- Space: O(1), only three integer variables for indices.

---

## 2. Number of 1 Bits (Hamming Weight)

**Problem:**  
Given a positive integer `n`, return the number of '1' bits (set bits) in its binary representation.

**Constraints:**  
- 0 ≤ n ≤ 2^31 - 1  

**Approach:**  
- While `n` is not zero, repeatedly unset the rightmost set bit.  
- Increment the count each time.  
- This operation is known as Brian Kernighan’s algorithm.

**Complexity:**  
- Time: O(k), where k is the number of set bits in `n`.  
- Space: O(1), just for the counter.

---
