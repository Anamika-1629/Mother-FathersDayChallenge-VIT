class Solution(object):
    def convertToTitle(self, columnNumber):
        lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
               'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        col_title = ''
        a = 26
        while columnNumber > 0:
            columnNumber -= 1
            b = columnNumber % a
            col_title = lst[b] + col_title
            columnNumber //= a
        return col_title

if __name__ == "__main__":
    columnNumber = int(input())
    print(Solution().convertToTitle(columnNumber))
