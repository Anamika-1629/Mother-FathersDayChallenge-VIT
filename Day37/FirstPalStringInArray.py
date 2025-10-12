class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""

    @staticmethod
    def main():
        words = input().strip().split()
        sol = Solution()
        print(sol.firstPalindrome(words))

if __name__ == "__main__":
    Solution.main()
