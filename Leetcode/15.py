'''
思路：

'''


class Solution:
    def threeSum(self, nums):
        nums.sort()
        num3_list = [-1 * i for i in nums]
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                print("num[{0}] = {1}     --    num[{2}] = {3}".format(i, nums[i], j, nums[j]))
                target = sorted([nums[i], nums[j], -1 * (nums[i] + nums[j])])
                if nums[i] + nums[j] in num3_list[j + 1:] and target not in result:
                    result.append(target)
        return result


if __name__ == '__main__':
    nums = [0, 0, 0]
    # nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    result = solution.threeSum(nums)
    print('=' * 60)
    for i in result:
        print(i)
