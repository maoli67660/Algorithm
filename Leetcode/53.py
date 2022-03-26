class Solution:
    def maxSubArray(self, nums):
        min_sum = min(0, nums[0])
        max_substr = nums[0]
        sum = nums[0]
        for i in range(1, len(nums)):
            sum = sum + nums[i]
            max_substr = max(sum - min_sum, max_substr)
            min_sum = min(min_sum, sum)
        return max_substr


if __name__ == '__main__':
    obj = Solution()
    print(obj.maxSubArray([1, -2]))

'''



[-2,-1, -4, 0, -1, 1, 2, -3, 1]
            i         )

[ 1, 3,  2, 5,  1, 2, 0, -1, 4]
            (
'''
