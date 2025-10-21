# Coding Challenge Solutions

Day 46 problems.

---

## 1. Prime Number of Set Bits in Binary Representation (762)

**Problem:**
Given two integers `left` and `right`, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

**Constraints:**
- 1 is less than or equal to left, which is less than or equal to right, which is less than or equal to     10^6.
- The number of set bits won't exceed 20 (since 2^{20} > 10^6).

**Approach:**
- Pre-calculate or hardcode the set of small prime numbers (up to 20): {2, 3, 5, 7, 11, 13, 17, 19}.
- Iterate through every number `i` from `left` to `right`.
- For each number, count its set bits.
- If the count of set bits is in the prime set, increment the total count.

**Complexity:**
- Time: O(right - left). The bit counting is O(1).
- Space: O(1), for storing the fixed set of primes.

---

## 2. Find Center of Star Graph (1791)

**Problem:**
Given an undirected star graph and its edges, find and return the center node.

**Constraints:**
- The input is guaranteed to be a star graph.

**Approach:**
- The center node is the only node present in every single edge.
- Check only the first two edges, edges[0] = [u_1, v_1] and edges[1] = [u_2, v_2].
- The common node between these two edges must be the center.
- Check if u_1 is equal to u_2 or v_2. If yes, u_1 is the center.
- Otherwise, v_1 must be the center.

**Complexity:**
- Time: O(1), as we perform a constant number of comparisons.
- Space: O(1).

---