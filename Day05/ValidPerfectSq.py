class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = num ** 0.5
        if a.is_integer():
            return True
        else:
            return False

def main():
    sol = Solution()
    
    # Example test cases
    test_numbers = [16, 14, 1, 25, 26, 100]

    for num in test_numbers:
        print(f"{num} -> {sol.isPerfectSquare(num)}")

if __name__ == "__main__":
    main()
