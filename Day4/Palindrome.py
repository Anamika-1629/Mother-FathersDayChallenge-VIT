class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = str(x)
        a = ''
        b = ''
        for i in temp:
            a += i
        for j in range(len(temp)-1, -1, -1):
            b += temp[j]
        if a == b:
            return True
        else:
            return False

def main():
    solution = Solution()
    test_cases = [121, -121, 10, 545, 12321, 278]
    
    for num in test_cases:
        print(f"{num} is palindrome? {solution.isPalindrome(num)}")

if __name__ == "__main__":
    main()