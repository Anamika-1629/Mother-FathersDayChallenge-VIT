class Solution(object):
    def countOdds(self, low, high):
        if low % 2 != 0 or high % 2 != 0:
            return ((high - low) // 2) + 1
        else:
            return (high - low) // 2

if __name__ == "__main__":
    low = int(input("Enter low: "))
    high = int(input("Enter high: "))
    sol = Solution()
    print(sol.countOdds(low, high))
