class Solution(object):
    def evalRPN(self, tokens):
        i = 0
        while len(tokens) > 1:
            if tokens[i] in "+-*/":
                a = int(tokens[i - 2])
                b = int(tokens[i - 1])
                if tokens[i] == "+":
                    c = a + b
                elif tokens[i] == "-":
                    c = a - b
                elif tokens[i] == "*":
                    c = a * b
                else:
                    c = int(float(a) / b)
                tokens[i] = str(c)
                del tokens[i - 1]
                del tokens[i - 2]
                i -= 1
            else:
                i += 1
        return int(tokens[0])

if __name__ == "__main__":
    tokens = input("Enter tokens as space-separated values (e.g. 2 1 + 3 *): ").split()
    print(Solution().evalRPN(tokens))
