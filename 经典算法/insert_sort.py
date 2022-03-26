'''

        解题报告。

注意的点：
    while 语句是满足条件 run。

'''


def insert_sort(arr):
    if len(arr) == 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        print(i, ' : ', arr)
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = key
    return arr


if __name__ == '__main__':
    print(insert_sort([1, 3, 2]))
