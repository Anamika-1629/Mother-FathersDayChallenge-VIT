class Solution(object):
    def trailingZeroes(self, n):
        a = 1
        for i in range(n, 0, -1):
            a *= i

        count = 0
        for i in str(a)[::-1]:
            if i == '0':
                count += 1
            else:
                break
        return count

if __name__ == "__main__":
    n = int(input("Enter n: "))
    sol = Solution()
    print(sol.trailingZeroes(n))
