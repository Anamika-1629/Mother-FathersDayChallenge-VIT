class Solution(object):
    def numberOfSubstrings(self, s):
        count = 0
        last_a = last_b = last_c = -1
        for i, char in enumerate(s):
            if char == 'a':
                last_a = i
            elif char == 'b':
                last_b = i
            else:
                last_c = i
            if last_a != -1 and last_b != -1 and last_c != -1:
                min_last = min(last_a, last_b, last_c)
                count += min_last + 1
        return count

if __name__ == "__main__":
    s = input().strip()
    sol = Solution()
    print(sol.numberOfSubstrings(s))
