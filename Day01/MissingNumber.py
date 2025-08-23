class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

def main():
    sol = Solution()
    test_cases = [
        [3, 0, 1],   
        [0, 1],          
        [9,6,4,2,3,5,7,0,1] 
    ]
    for i, nums in enumerate(test_cases, 1):
        print(f"Test case {i}: Input: {nums}")
        print(f"Missing number: {sol.missingNumber(nums)}")
        print()

if __name__ == "__main__":
    main()
