class Solution(object):
    def isGoodArray(self, nums):
        res = nums[0]
        for num in nums[1:]:
            a, b = res, num
            while b:
                a, b = b, a % b
            res = a
            if res == 1:
                return True
        return res == 1

if __name__ == "__main__":
    nums = list(map(int, input().strip().strip('[]').split(',')))
    sol = Solution()
    print(sol.isGoodArray(nums))
