class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sign = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                sign = 0
            elif nums[i] < 0:
                sign *= -1
            else:
                sign *= 1
        return sign

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    print(Solution().arraySign(nums))
