class Solution(object):
    def gcdOfStrings(self, str1, str2):
        a, b = len(str1), len(str2)
        while b:
            a, b = b, a % b
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:a]

if __name__ == "__main__":
    str1 = input().strip()
    str2 = input().strip()
    sol = Solution()
    print(sol.gcdOfStrings(str1, str2))
