class Solution(object):
    def hammingDistance(self, x, y):
        xor = x ^ y
        count = 0
        while xor:
            xor &= xor - 1
            count += 1
        return count

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    sol = Solution()
    print(sol.hammingDistance(x, y))
