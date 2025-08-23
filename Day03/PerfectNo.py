class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
            
        s = 1  
        n = int(num**0.5) + 1
        
        for i in range(2, n):
            if num % i == 0:
                s += i
                c = num // i
                if c != i:
                    s += c
                if s > num:
                    return False
        
        return s == num

def main():
    sol = Solution()
    tests = [6, 28, 496, 8128, 5, 12, 33550336]
    for n in tests:
        res = sol.checkPerfectNumber(n)
        print(f"{n}: {'Perfect' if res else 'Not perfect'}")

if __name__ == "__main__":
    main()