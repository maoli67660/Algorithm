'''

思路：
注意负数问题
'''

class Solution:
    def maximumProduct(self, nums):
        nums.sort()

        def product_3(arr):
            result = 1
            for i in arr:
                result = result * i
            return result

        return max([product_3(nums[-3:]), product_3(nums[:3]), product_3(nums[:2] + nums[-1:])])
