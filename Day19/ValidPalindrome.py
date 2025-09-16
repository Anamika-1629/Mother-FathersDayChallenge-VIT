class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == '__main__':
    solution = Solution()
    s1 = "()[]{}"
    s2 = "([)]"
    print(f"String: {s1}, Is Valid: {solution.isValid(s1)}")
    print(f"String: {s2}, Is Valid: {solution.isValid(s2)}")