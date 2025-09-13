class Solution(object):
    def twoSum(self, nums, target):
        out_list = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    out_list = [i, j]
                    return out_list
        return out_list

def main():
    n = int(input("Enter array size: "))
    nums = list(map(int, input("Enter array elements: ").split()))
    target = int(input("Enter target: "))
    sol = Solution()
    result = sol.twoSum(nums, target)
    print("Indices:", result)

if __name__ == "__main__":
    main()
