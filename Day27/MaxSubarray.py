class Solution(object):
    def maxSubArray(self, nums):
        curr = res = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            res = max(res, curr)
        return res

if __name__ == "__main__":
    nums = list(map(int, input("Enter elements separated by space: ").split()))
    sol = Solution()
    print(sol.maxSubArray(nums))
