'''

思路：
从上一个状态n 迭代出下一个状态n
用set判断序列是否有环

注意点：
    闭包的使用
    函数中定义函数
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            next_n = 0
            while n > 0:
                n, digit = divmod(n, 10)
                next_n = next_n + digit ** 2
            return next_n

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(1309))
