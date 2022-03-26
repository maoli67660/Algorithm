class Solution:
    def shortestPalindrome(self, s):
        if s == "":
            return ""
        elif len(s) == 1:
            return s
        # time complexity O(n)
        def isPalidrom(ss):
            mid_index = int(len(ss) / 2)
            if len(ss) % 2 == 1:
                i, j = mid_index, mid_index
            else:
                i, j = mid_index - 1, mid_index
                if ss[i] != ss[j]:
                    return False
            while i > 0 and j < len(ss) - 1:
                i -= 1
                j += 1
                if ss[i] != ss[j]:
                    return False
            return True

        index = 0
        max_index = 0
        while index < len(s):
            if isPalidrom(s[:index + 1]):
                max_index = index
            index += 1
        return s[max_index + 1:][::-1] + s


if __name__ == '__main__':
    solution = Solution()
    assert solution.shortestPalindrome("") == ""
    assert solution.shortestPalindrome("a") == "a"
    #print("ab -- > ", solution.shortestPalindrome("ab"))
    assert solution.shortestPalindrome("ab") == "bab"

    assert solution.shortestPalindrome("bba") == "abba"
    assert solution.shortestPalindrome("bcba") == "abcba"
