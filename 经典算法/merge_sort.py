'''

        解题报告。

注意的点：


'''


def merge(arr, left, mid, right):
    i = left
    j = mid

    while i < mid or j <= right:
        if (i < mid and arr[i] < arr[j]) or j > right:
            pass






def merge_sort(arr, left, right):
    if left < right:
        mid = int((left + right) / 2)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


if __name__ == '__main__':
    arr = [3, 1, 4, 1, 5, 9]
    print(merge_sort(arr, left=0, right=len(arr) - 1))
