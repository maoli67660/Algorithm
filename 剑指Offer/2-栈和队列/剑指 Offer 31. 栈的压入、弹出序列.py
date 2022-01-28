class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        for item in pushed:
            stack.append(item)
            while len(stack) > 0 and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)
        return stack == popped[::-1]
