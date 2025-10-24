class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    solution = Solution()
    print(solution.singleNumber(nums))
