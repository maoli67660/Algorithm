class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_before = len(nums)
        while 0 in nums:
            nums.remove(0)

        zeros_num = len_before - len(nums)
        nums += [0] * zeros_num


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)
