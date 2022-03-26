#没做出来

class Solution:
    def productExceptSelf(self, nums):
        left_pow = []
        pow_all = 1
        for i in nums:
            left_pow.append(pow_all * i)
            pow_all = pow_all * i

        right_pow = []
        pow_all = 1
        for i in range(len(nums) - 1, -1, -1):
            right_pow.append(pow_all * nums[i])
            pow_all = pow_all * nums[i]
        right_pow.reverse()

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right_pow[0])
            elif i == len(nums) - 1:
                result.append(left_pow[len(nums) - 2])
            else:
                result.append(left_pow[i - 1] * right_pow[i + 1])

        return result


if __name__ == '__main__':
    nums = [4, 3, 2, 1, 2]
    solution = Solution()
    print(solution.productExceptSelf(nums))
