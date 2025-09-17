class Solution(object):
    def checkValidString(self, s):
        low = high = 0
        for c in s:
            if c == '(':
                low += 1
                high += 1
            elif c == ')':
                low -= 1
                high -= 1
            else:
                low -= 1
                high += 1
            if high < 0:
                return False
            if low < 0:
                low = 0
        return low == 0

if __name__ == "__main__":
    s = input("Enter string: ")
    print(Solution().checkValidString(s))
