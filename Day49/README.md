# Coding Challenge Solutions

Day 49 problems.

---

## 1. Single Number

**Problem:**  
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

**Constraints:**  
- 1 ≤ nums.length ≤ 3 × 10^4  
- Each element in the array appears twice except for one.

**Approach:**  
- Use the XOR operation: iterate through the array, XORing all elements.
- Since  
  - x ^ x = 0  
  - x ^ 0 = x  
- All duplicate elements will cancel out, leaving just the unique element.

**Complexity:**  
- Time: O(n), where n is the length of the array.  
- Space: O(1), using just one variable to hold the XOR result.

---

## 2. Count Primes

**Problem:**  
Given an integer n, return the number of prime numbers that are strictly less than n.

**Constraints:**  
- 0 ≤ n ≤ 5 × 10^6

**Approach:**  
- Use the Sieve of Eratosthenes algorithm:
  - Create a boolean array representing primality for all numbers less than n.
  - Initially set all entries (except 0, 1) as true.
  - For each i starting from 2, mark all multiples of i as not prime.
  - Count how many values remained true (prime) at the end.

**Complexity:**  
- Time: O(n log log n), efficient for large n.
- Space: O(n), for the boolean sieve array.

---
