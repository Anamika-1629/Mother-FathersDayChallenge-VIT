def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate

if __name__ == "__main__":
    nums = [3, 2, 3]
    print(majorityElement(nums))  
