def findDuplicate(nums):
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

if __name__ == "__main__":
    nums = list(map(int, input("Enter array: ").split()))
    print(findDuplicate(nums))
