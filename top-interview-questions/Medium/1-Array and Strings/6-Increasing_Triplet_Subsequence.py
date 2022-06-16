
'''
https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
'''
from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    small = mid = float('inf')

    for i in nums:
        if i < small:
            small = i
        elif i > small and i < mid:
            mid = i
        elif small < mid and mid < i:
            return True
    return False


if __name__ == '__main__':
    # assert increasingTriplet([1, 2, 3, 4, 5])
    # assert increasingTriplet([2, 1, 5, 0, 4, 6])
    # assert not increasingTriplet([5, 4, 3, 2, 1])

    assert not increasingTriplet([2, 1, 5, 0, 3])
