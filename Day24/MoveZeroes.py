class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums) - count:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1

if __name__ == "__main__":
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
    Solution().moveZeroes(nums)
    print(nums)
