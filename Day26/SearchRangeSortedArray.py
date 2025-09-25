from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findIndex(isFirst):
            left, right = 0, len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    idx = mid
                    if isFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return idx
        start = findIndex(True)
        end = findIndex(False)
        return [start, end]

if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    nums = list(map(int, input("Enter sorted array elements: ").split()))
    target = int(input("Enter target value: "))
    sol = Solution()
    result = sol.searchRange(nums, target)
    print("First and Last Position:", result)
