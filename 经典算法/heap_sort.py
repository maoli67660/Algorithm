'''

        解题报告。

写的非常不满意。 heap_pop出错
while 循环的结构上：
1. 判断是否有左孩子，  是否和左孩子交换
2. 判断是否有右孩子， 是否和右孩子交换
如果都不交换， 提前结束

heap_pop出错
比较右左子树， 指针已经更新了。 再去操作右子树
对变量修改检查不到位。 需要训练

'''


def get_parent(index):
    return int(index / 2)


def get_kids(index):
    return 2 * index, 2 * index + 1


def heap_push(arr, key):
    arr.append(key)
    index = len(arr) - 1
    while index != 1:
        parent = get_parent(index)
        if arr[index] < arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]
        index = parent


def heap_pop(arr):
    key = arr[1]
    arr[1] = arr[len(arr) - 1]
    del arr[len(arr) - 1]
    index = 1
    while index * 2 < len(arr) - 1:  # 判断是否左孩子
        #print('index = ', index, '      arr=',arr)
        left_kid, right_kid = get_kids(index)
        end_flag = True
        if arr[index] > arr[left_kid]:
            #print('left exchange: ', arr[index], '   and  ', arr[left_kid])
            arr[index], arr[left_kid] = arr[left_kid], arr[index]
            next_index = left_kid
            end_flag = False
        if right_kid < len(arr) and arr[index] > arr[right_kid]:
            #print('right exchange: ', arr[index], '   and  ', arr[right_kid])
            arr[index], arr[right_kid] = arr[right_kid], arr[index]
            next_index = right_kid
            end_flag = False

        index = next_index
        if end_flag:
            break
    return key


if __name__ == '__main__':
    arr = [0]
    heap_push(arr, 3)
    heap_push(arr, 1)
    heap_push(arr, 4)
    heap_push(arr, 1)
    heap_push(arr, 5)
    heap_push(arr, 9)

    print(arr)
    print('----------------')
    print(heap_pop(arr))
    print(heap_pop(arr))
    print(heap_pop(arr))
    # print("***************")
    # print(arr)
    # print("***************")
    print(heap_pop(arr))
    print(heap_pop(arr))

    print(heap_pop(arr))
