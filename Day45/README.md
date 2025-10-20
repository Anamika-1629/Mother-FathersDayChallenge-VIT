# Coding Challenge Solutions

Day 45 problems.

---

## 1. Find the Town Judge

**Problem:**  
There are n people in a town, labeled from 1 to n. Some people trust others. The town judge is trusted by everyone else, but trusts nobody. Given the trust relationships, find the judge or return -1 if they don't exist.

**Constraints:**  
- The judge trusts nobody.
- Everybody (except the judge) trusts the judge.
- n is between 1 and 1000.
- Trust is a list of pairs [a, b] meaning person a trusts person b.

**Approach:**  
- Use an array to count trust scores for each person.
- Subtract 1 from a person's score when they trust someone.
- Add 1 to a person's score when they are trusted by someone.
- The judge will have a score of n-1, everyone else will not.

**Complexity:**  
- Time: O(T + n), where T is the length of the trust list.
- Space: O(n), for the count array.

---

## 2. Greatest Common Divisor of Strings

**Problem:**  
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2 (i.e., both are made by concatenating x with itself one or more times). If no such string exists, return an empty string.

**Constraints:**  
- str1 and str2 consist of uppercase English letters.
- 1 ≤ str1.length, str2.length ≤ 1000

**Approach:**  
- Use the Euclidean algorithm on their lengths to find the potential GCD length.
- If concatenating in both orders produces the same string, the GCD string exists.
- Otherwise, return an empty string.

**Complexity:**  
- Time: O(m + n), where m and n are the lengths of str1 and str2.
- Space: O(m + n), due to concatenation for comparison.

---