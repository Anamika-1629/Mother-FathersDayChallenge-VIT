class Solution(object):
    def subarrayLCM(self, nums, k):
        count = 0
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr > k or k % curr != 0:
                continue
            for j in range(i, n):
                if i != j:
                    a, b = curr, nums[j]
                    while b != 0:
                        a, b = b, a % b
                    curr = (curr * nums[j]) // a
                if curr == k:
                    count += 1
                elif curr > k:
                    break
        return count

if __name__ == "__main__":
    nums = list(map(int, input("Enter array elements separated by space:\n").split()))
    k = int(input("Enter k:\n"))
    sol = Solution()
    print("Number of subarrays with LCM equal to k:", sol.subarrayLCM(nums, k))
