# Coding Challenge Solutions

Day 11 problems.

---

## 1. Factorial Trailing Zeroes (LeetCode 172)

**Problem:**  
Given an integer \( n \), return the number of trailing zeroes in \( n! \).

--

**Constraints:**  
- \( 0 \leq n \leq 10^9 \) (efficient approach needed, factorial too large to compute directly)

--

**Approach:**  
- Count factors of 5 in \( n! \), because each zero is contributed by a factor pair of 2 and 5 and there are abundant 2s.
- Repeatedly divide \( n \) by 5, adding quotients until \( n < 5 \).

--

**Complexity:**  
- Time: O(log_5 n)  
- Space: O(1)

---

## 2. Remove Nth Node From End of List (LeetCode 19)

**Problem:**  
Given the head of a linked list, remove the \( n \)th node from the end of the list and return its head.

--

**Constraints:**  
- The number of nodes in the list is in the range [1, 10^5]  
- 1 <= n <= size of the list

--

**Approach:**  
- Use two pointers with a gap of \( n \) nodes.  
- Move both pointers until the leading pointer reaches the end.  
- Remove the node by bypassing it.

--

**Complexity:**  
- Time: O(list length)  
- Space: O(1)

---