import math

class Solution(object):
    def bulbSwitch(self, n):
        return int(math.sqrt(n))

if __name__ == "__main__":
    n = int(input("Enter n: "))
    sol = Solution()
    print(sol.bulbSwitch(n))
