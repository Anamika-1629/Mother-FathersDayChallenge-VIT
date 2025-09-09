class Solution(object):
    def reverse(self, x):
        temp = str(abs(x))
        y = ''
        for i in range(len(temp) - 1, -1, -1):
            y += temp[i]
        y = int(y)
        if x < 0:
            y = -y
        if y < -2**31 or y > 2**31 - 1:
            return 0
        return y

if __name__ == "__main__":
    x = int(input())
    sol = Solution()
    print(sol.reverse(x))
