class Solution(object):
    def reverseWords(self, s):
        temp = s.split()
        temp.reverse()
        return ' '.join(temp)

if __name__ == "__main__":
    s = input().strip()
    sol = Solution()
    print(sol.reverseWords(s))
