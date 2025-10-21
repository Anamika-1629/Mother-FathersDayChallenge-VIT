class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

if __name__ == "__main__":
    n = int(input().strip())
    sol = Solution()
    print(sol.hammingWeight(n))
