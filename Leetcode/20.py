class Solution:
    def isValid(self, s):
        match_dict = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for i in s:
            if i in match_dict:
                stack.append(i)
            elif len(stack) > 0 and match_dict[stack[-1]] == i:
                stack.pop()
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    result = solution.isValid('}{')
    print(result)
