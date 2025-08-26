class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        l = len(columnTitle)
        col_no = 0
        a = ''
        b = 0
        c = 0
        for i in range(l-1,-1,-1):
            a = columnTitle[i]
            for j in range(len(lst)):
                if lst[j] == a:
                    b = j+1
                    break
            col_no += b*(26**c)
            c += 1
        return col_no

if __name__ == "__main__":
    columnTitle = input("Enter Excel column title: ")
    sol = Solution()
    print("Column number is:", sol.titleToNumber(columnTitle))
