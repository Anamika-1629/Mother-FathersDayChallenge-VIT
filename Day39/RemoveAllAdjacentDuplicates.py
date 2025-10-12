class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)

    @staticmethod
    def main():
        s = input().strip()
        sol = Solution()
        print(sol.removeDuplicates(s))

if __name__ == "__main__":
    Solution.main()
