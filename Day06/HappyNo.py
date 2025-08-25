class Solution(object):
    def isHappy(self, n):
        l = []
        while n != 1 and n not in l:
            l.append(n)
            b = 0
            for i in str(n):
                b += int(i) ** 2
            n = b
        return n == 1

def main():
    sol = Solution()
    test_cases = [19, 2, 7, 20]
    for n in test_cases:
        print(f"isHappy({n}) = {sol.isHappy(n)}")

if __name__ == "__main__":
    main()
