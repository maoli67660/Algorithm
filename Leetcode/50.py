class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        result = 1
        while n:
            if n % 2:
                result *= x

            x = x * x
            n = n >> 1
        return result


class Solution2:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return self.myPow(x, n - 1) * x
        return self.myPow(x * x, n >> 1)


if __name__ == '__main__':
    solution = Solution()
    print(solution.myPow(2, 2))
