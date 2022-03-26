class Solution:
    def decodeString(self, s):
        numset = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        def getNumStr(left_index):
            index = left_index - 1
            while s[index] in numset:
                index = index - 1
            return s[index + 1:left_index]

        def get_first_bracket_i(left_index):
            for index in range(left_index, len(s)):
                if s[index] == '[':
                    return index
            return index

        def get_right_bracket_i(left_index):
            stack = ['[']
            right_index = left_index
            while stack:
                right_index = right_index + 1
                if s[right_index] == ']':
                    stack.pop()
                elif s[right_index] == '[':
                    stack.append('[')
            return right_index

        if '[' not in s:
            return s
        left_index = 0
        while left_index < len(s) - 3:
            left_index = get_first_bracket_i(left_index)
            right_index = get_right_bracket_i(left_index)
            num = int(getNumStr(left_index))
            decode = self.decodeString(s[left_index + 1: right_index]) * num
            s = s[:left_index - len(str(num))] + decode + s[right_index + 1:]
            left_index = left_index + len(decode) - 1
        return s


if __name__ == '__main__':
    solution = Solution()

    print(solution.decodeString("abc3[cd]xyz"))
