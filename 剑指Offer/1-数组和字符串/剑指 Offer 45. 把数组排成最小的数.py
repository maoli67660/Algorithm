class numstr:
    def __init__(self, val):
        self.val = str(val)
    def __lt__(self, other):
        return self.val + str(other) < str(other) + self.val
    def __repr__(self):
        return str(self.val)

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        ls = sorted([numstr(n) for n in nums])
        ls2 = [i.val for i in ls ]
        return ''.join(ls2)

