class Solution:
    def twoCitySchedCost(self, costs):
        def min_and_index(pair):
            if pair[0] < pair[1]:
                return 0, pair[0]
            else:
                return 1, pair[1]

        costs.sort(key=lambda x: max(x[0], x[1]) - min(x[0], x[1]), reverse=True)
        print(costs)
        N = int(len(costs) / 2)
        city_count = [N, N]
        total_cost = 0
        for item in costs:
            min_index, cost = min_and_index(item)
            if city_count[min_index] > 0:
                city_count[min_index] -= 1
                total_cost += cost
            else:
                city_count[1 - min_index] -= 1
                total_cost += item[1 - min_index]
        return total_cost


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoCitySchedCost(
        [[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
    print("result = ", result)
