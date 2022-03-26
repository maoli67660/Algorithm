import heapq


class Solution:
    def highFive(self, items):
        dic_it = {}
        for item in items:
            if item[0] not in dic_it:
                dic_it[item[0]] = []
            dic_it[item[0]].append(item[1])

        result = []
        print(dic_it)
        for key in dic_it:
            heapq.heapify(dic_it[key])
            ls = heapq.nlargest(5, dic_it[key])
            result.append([key, int(sum(ls) / len(ls))])
        return result


if __name__ == '__main__':
    ls = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
    solution = Solution()
    result = solution.highFive(ls)
    print(result)
