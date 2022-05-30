from typing import List


    """
    26. 删除排序数组中的重复项 难度：简单
    给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

    不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    思路： 遍历数组， 如果和右边相邻元素相等，删除当前元素。否则继续向前搜索
    """
def remove_duplicates(nums):
    fast, slow = 0, 0
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast+=1
        else:
            slow+=1
            nums[slow] = nums[fast]
    return nums[:slow+1]

if __name__ == '__main__':
    assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == [0, 1, 2, 3, 4]
    assert remove_duplicates([1, 1, 2, 3]) == [1, 2, 3]
