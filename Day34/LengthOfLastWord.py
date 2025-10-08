class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        return count

if __name__ == "__main__":
    s = input("Enter the string: ")
    print(Solution().lengthOfLastWord(s))
