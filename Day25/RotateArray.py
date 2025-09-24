class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        l1 = nums[n - k:]
        l2 = nums[:n - k]
        l1.extend(l2)
        nums[:] = l1

if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by space: ").split()))
    k = int(input("Enter k: "))
    Solution().rotate(nums, k)
    print("Rotated array:", nums)
