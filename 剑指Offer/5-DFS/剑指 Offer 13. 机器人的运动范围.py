class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        visited = set()

        def dfs(x, y, m, n, k):
            if x >= m or y >= n or (x, y) in visited or x % 10 + x // 10 + y % 10 + y // 10 > k:
                return 0
            visited.add((x, y))
            return 1 + dfs(x + 1, y, m, n, k) + dfs(x, y + 1, m, n, k)

        return dfs(0, 0, m, n, k)


if __name__ == '__main__':
    solution = Solution()
    res = solution.movingCount(2, 3, 1)
    print(f'-----  result: {res}  -----')
