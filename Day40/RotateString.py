class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        doubled = s + s
        if goal in doubled:
            return True
        else:
            return False

    @staticmethod
    def main():
        s = input().strip()
        goal = input().strip()
        sol = Solution()
        print(sol.rotateString(s, goal))

if __name__ == "__main__":
    Solution.main()
