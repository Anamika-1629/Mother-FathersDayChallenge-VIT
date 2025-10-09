class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        a = list(s)
        b = []
        c = []
        for i in range(len(a)):
            if a[i] in vowels:
                b.append(a[i])
                c.append(i)
        b.reverse()
        for i in range(len(c)):
            a[c[i]] = b[i]
        return ''.join(a)

if __name__ == "__main__":
    s = input("Enter the string: ")
    print(Solution().reverseVowels(s))
