class Solution(object):
    def countSegments(self, s):
        return len(s.split())

if __name__ == "__main__":
    s = input("Enter the string: ")
    print(Solution().countSegments(s))
