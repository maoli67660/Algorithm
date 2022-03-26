'''
解题报告末班：
*算法
    1.用的什么算法
    2.为什么用

*代码
    1. 注意的点
        1.1 Binary search:
            如果查询不到， 返回 大于（小于）key的坐标。  每一个元素都比可以大（小）返回什么？
        1.2 开始结束条件
        1.3 单元测试的能力
    2. 可以优化的地方

* 时空复杂度分析

*做过相关的题有哪些
'''


def vertical_serach(matrix, left_point, target):
    print('----v---')
    left = 0
    right = len(matrix) - 1

    while left < right:
        mid = math.ceil((left + right) / 2)

        if matrix[mid][left_point] > target:
            right = mid - 1
        elif matrix[mid][left_point] == target:
            return left, True
        else:
            left = mid

    if matrix[left][left_point] == target:
        return left, True
    else:
        return left, False


''''
return first item larget than the target
-1  -> 0
0  -> 0
0.5  -> 1
1  -> 1
1.5 -> 1
'''
import math


def horizontal_serach(matrix, low_point, target):
    print('----h---')
    left = 0
    right = len(matrix[0]) - 1

    while left < right:
        mid = int((left + right) / 2)
        print("matrix[low_point][mid] = ", matrix[low_point][mid])
        print("left ", left, ' right ', right, 'mid:', mid)
        if matrix[low_point][mid] < target:
            left = mid + 1
        elif matrix[low_point][mid] == target:
            return left, True
        else:
            right = mid

    if matrix[low_point][left] == target:
        return left, True
    else:
        return left, False


def searchMatrix(matrix, target):
    max_y = len(matrix) - 1
    max_x = len(matrix[0]) - 1
    left_point, low_point = 0, max_y

    if matrix == []:
        return False
    elif matrix == [[]]:
        return False

    while low_point != 0 and left_point != max_x:
        print('left_point: ', left_point, 'low_point: ', low_point)

        low_point, found = vertical_serach(matrix, left_point, target)
        if found:
            return True
        left_point, found = horizontal_serach(matrix, low_point, target)
        if found:
            return True

    print('Finally   low_point:', low_point, '   left_point:', left_point)
    if low_point == 0:
        return horizontal_serach(matrix, low_point, target)[1]
    else:
        return vertical_serach(matrix, left_point, target)[1]


if __name__ == '__main__':
    matrix = [[1], [3]]

result = searchMatrix(matrix, target=4)

print("searchMatrix result = ", result)
