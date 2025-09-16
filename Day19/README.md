# Coding Challenge Solutions

Day 19 problem.

---

## 1. Best Time to Buy and Sell Stock (LeetCode 121)

**Problem:** 
You're given an array of stock prices, where `prices[i]` is the price on a given day. Your goal is to **maximize your profit** by buying on one day and selling on a different, future day. If no profit can be made, return `0`.

**Constraints:** 
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

**Approach:** 
- Iterate through the prices while keeping track of the **lowest price** seen so far.
- For each day, calculate the potential profit by subtracting the current minimum price from the current price.
- Update the **maximum profit** found with this potential profit if it's greater.
- The minimum price is also updated if a new, lower price is encountered. This ensures you're always considering the best possible buying point for a future sale.

**Complexity:** 
- Time:O(n), as you only need to iterate through the array once.
- Space: O(1), since you only use a few variables to track the minimum price and maximum profit.

---

## 2. Valid Parentheses (LeetCode 20)

**Problem:** 
Given a string `s` containing just the characters `(`, `)`, `{`, `}`, `[`, and `]`, determine if the input string is valid. A valid string has matching and correctly ordered opening and closing brackets.

**Constraints:** 
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only.

**Approach:** 
- Use a **stack** to keep track of opening brackets.
- Iterate through each character of the string. If it's an opening bracket, push it onto the stack.
- If it's a closing bracket, check if the stack is not empty and if the top of the stack is its corresponding opening bracket.
- If they match, pop from the stack. If not, or if the stack is empty, the string is invalid.
- After iterating through the entire string, the stack should be empty if all brackets were correctly matched.

**Complexity:** 
- Time: O(n), where `n` is the length of the string, as you process each character once.
- Space: O(n), in the worst-case scenario where all characters are opening brackets, and they all have to be stored in the stack.

---