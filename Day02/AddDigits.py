class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            while num >= 10:
                a = str(num)
                b = 0
                l = []
                for i in a:
                    l.append(int(i))
                for j in l:
                    b += j
                num = b
            return num

def main():
    sol = Solution()
    
    test_cases = [0, 38, 123, 9999]
    
    for i, num in enumerate(test_cases, 1):
        result = sol.addDigits(num)
        print(f"Test case {i}: Input: {num} -> Output: {result}")

if __name__ == "__main__":
    main()
