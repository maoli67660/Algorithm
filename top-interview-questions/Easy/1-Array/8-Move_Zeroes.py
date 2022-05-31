'''
LeetCode 283. 移动零(简单)
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f,s = 0,0
        while f <len(nums):
            if nums[f] != 0:
                nums[s] = nums[f]
                s+=1
            f+=1
        nums[s:] = [0] * len(nums[s:])

if __name__ == '__main__':
    assert moveZeroes([0, 0, 1]) == [1, 0, 0]
    assert moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
