class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ''
        for i in digits:
            a += str(i)
        b = int(a) + 1
        l = []
        for j in str(b):
            l.append(int(j))
        return l

def main():
    sol = Solution()
    test_cases = [
        [1, 2, 3],
        [9],
        [4, 3, 2, 1],
        [0]
    ]
    for digits in test_cases:
        print(f"plusOne({digits}) = {sol.plusOne(digits)}")

if __name__ == "__main__":
    main()
