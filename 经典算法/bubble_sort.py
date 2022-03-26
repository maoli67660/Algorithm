'''

        解题报告。

注意的点：
    range(start,end, step_size)

'''



def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    print(bubble_sort([1, 3, 2]))
