class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        is_prime = [True] * n
        is_prime[0:2] = [False, False]
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                is_prime[i*i:n:i] = [False] * len(is_prime[i*i:n:i])
        return sum(is_prime)

if __name__ == "__main__":
    n = int(input())
    solution = Solution()
    print(solution.countPrimes(n))
