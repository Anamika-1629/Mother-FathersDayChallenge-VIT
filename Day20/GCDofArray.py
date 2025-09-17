class Solution(object):
    def findGCD(self, nums):
        mm = min(nums)
        mx = max(nums)
        for i in range(mm, 0, -1):
            if mm % i == 0 and mx % i == 0:
                return i
        return 1

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(Solution().findGCD(nums))
