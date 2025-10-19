class Solution(object):
    def maxVowels(self, s, k):
        vowels = 'aeiou'
        b = 0
        c = 0
        for i in range(k):
            if s[i] in vowels:
                b += 1
        c = b
        i = 1
        while i + k - 1 < len(s):
            if s[i - 1] in vowels:
                b -= 1
            if s[i + k - 1] in vowels:
                b += 1
            if b > c:
                c = b
            i += 1
        return c

if __name__ == "__main__":
    s = input().strip()
    k = int(input().strip())
    sol = Solution()
    print(sol.maxVowels(s, k))
