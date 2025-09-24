class Solution(object):
    def calculate(self, s):
        stack = []
        num = 0
        sign = 1
        res = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                res += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                res += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        return res + sign * num

if __name__ == "__main__":
    s = input("Enter expression: ")
    print(Solution().calculate(s))
