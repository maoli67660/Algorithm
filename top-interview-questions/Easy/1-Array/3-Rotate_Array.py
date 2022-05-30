'''
LeetCode 189. 旋转数组[中等难度]

给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
def roatate_arr(arr,left,right):
    i, j = left, right
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def rotate(nums, k):
    """
      Do not return anything, modify nums in-place instead.
    """
    roatate_arr(nums,0,len(nums)-1)
    roatate_arr(nums,0,k%len(nums)-1)
    roatate_arr(nums,k%len(nums),len(nums)-1)
    
# 一行过 nums[:] = nums[::-1][:k%len(nums)][::-1] + nums[::-1][k%len(nums):][::-1]

if __name__ == '__main__':
    assert rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate(nums=[-1,-100,3,99], k=2) == [3,99,-1,-100]
    
