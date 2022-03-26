class Solution:
    def allPathsSourceTarget(self, graph):

        def dfs(v):
            next_nodes = graph[v]
            if next_nodes:
                result_ls = []
                for i in next_nodes:
                    pre_result = dfs(i)
                    for result in pre_result:
                        result_ls.append([v] + result)
                return result_ls
            else:
                return [[v]]

        return dfs(0)


if __name__ == '__main__':
    solution = Solution()
    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    result = solution.allPathsSourceTarget(graph)
    print('*' * 50)
    print(result)
