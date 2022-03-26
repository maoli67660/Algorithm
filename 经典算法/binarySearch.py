'''
        解题报告。

注意的点：
mid 向上向 or下取整的问题
Bug Free 人肉单元测试用例
    [0] 搜索 -1,  -0.5,  0,  0.5,  1
    [0,1] 搜索  -1, 0, 0.5, 1, 2
'''


def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left < right:
        # print(left, right)
        mid = int((left + right) / 2)
        if key == arr[mid]:
            break
        elif key > arr[mid]:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    key = 5
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')

    arr = [1]
    key = 2
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')

    arr = [0, 1, 2]
    key = -1
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')

    arr = [3, 4, 5]
    key = 3
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')

    arr = [3, 4, 5]
    key = 3.5
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')

    arr = [3, 4, 5]
    key = 5
    print(arr, 'find {}: '.format(key), binary_search(arr, key))
    print('-----------------------')
