class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

    @staticmethod
    def main():
        import ast
        line = input().strip()
        strs = ast.literal_eval(line)
        sol = Solution()
        print(sol.longestCommonPrefix(strs))

if __name__ == "__main__":
    Solution.main()
