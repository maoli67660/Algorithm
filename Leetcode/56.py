# 没做完
class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        print("intervals:   ", intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            print(i, '    ', intervals[i])
            print('result:  ', result)
            if result[-1][1] < intervals[i][0]:
                result.append(intervals[i])
                print('         append', intervals[i])
            else:
                top = result.pop()
                result.append([top[0], max(intervals[i][1], top[1])] )
                print('         merge into', [top[0], max(intervals[i][1], top[1])])
        return result


if __name__ == '__main__':
    solution = Solution()
    input_list = [[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(input_list))
