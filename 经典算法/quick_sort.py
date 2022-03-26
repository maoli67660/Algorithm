'''

        解题报告。

注意的点：
    L13 L17 漏写条件 left<right

'''


def partion(arr, left, right):
    key = arr[left]
    while left < right:
        while arr[right] >= key and left < right:
            right = right - 1
        arr[left] = arr[right]

        while arr[left] <= key and left < right:
            left = left + 1
        arr[right] = arr[left]

    arr[left] = key
    return left


def quit_sort(arr, left, right):
    pillar = partion(arr, left, right)
    if pillar > left:
        quit_sort(arr, left, pillar - 1)
    if pillar < right:
        quit_sort(arr, pillar + 1, right)


if __name__ == '__main__':
    arr = [0]
    # print('partion', partion(arr, left=0, right=len(arr)-1))
    quit_sort(arr, left=0, right=len(arr) - 1)
    print(arr)
