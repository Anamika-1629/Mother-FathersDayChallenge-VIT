class Solution(object):
    def containsDuplicate(self, nums):
        temp = set()
        for num in nums:
            if num in temp:
                return True
            temp.add(num)
        return False

def main():
    nums = [1, 2, 3, 1]
    sol = Solution()
    print("Contains Duplicate:", sol.containsDuplicate(nums)) 
if __name__ == "__main__":
    main()
