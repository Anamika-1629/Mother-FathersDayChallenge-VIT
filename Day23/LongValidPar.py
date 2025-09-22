class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == '(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    max_len = max(max_len, i - st[-1])

        return max_len

if __name__ == '__main__':
    s = "(()"
    sol = Solution()
    print(sol.longestValidParentheses(s))  
