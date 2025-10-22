# Coding Challenge Solutions

Day 48 problems.

---

## 1. Check If It Is a Good Array

**Problem:**  
Given an array `nums` of positive integers, determine if there exists any subset of `nums` such that by multiplying each element by any integer and summing, you can obtain a sum of 1. Return True if the array is good, otherwise return False.

**Constraints:**  
- 1 ≤ nums.length ≤ 100000  
- 1 ≤ nums[i] ≤ 1000000000

**Approach:**  
- Compute the Greatest Common Divisor (GCD) of all entries in the array.
- If at any step the GCD is 1, return True immediately.
- By mathematical property, if the overall GCD is 1, it means 1 can be represented by some combination.
- Otherwise, after checking all elements, return whether the GCD is 1.

**Complexity:**  
- Time: O(n), where n is the size of the array.
- Space: O(1), constant extra variables.

---

## 2. Hamming Distance

**Problem:**  
Given two integers `x` and `y`, return the number of positions at which the corresponding bits are different (the Hamming distance).

**Constraints:**  
- 0 ≤ x, y < 2147483648

**Approach:**  
- XOR both numbers to find which bit positions differ.
- Count the set bits in the result.
- Efficiently count set bits using repeated bit manipulation.

**Complexity:**  
- Time: O(k), where k is the number of set bits in x xor y.
- Space: O(1), constant space for counter.

---