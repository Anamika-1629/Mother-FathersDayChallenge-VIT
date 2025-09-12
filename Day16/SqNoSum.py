class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(0, int(c ** 0.5) + 1):
            b_sq = c - a * a
            b = int(b_sq ** 0.5)
            if b * b == b_sq:
                return True
        return False

if __name__ == "__main__":
    c = int(input())
    sol = Solution()
    print(sol.judgeSquareSum(c))
