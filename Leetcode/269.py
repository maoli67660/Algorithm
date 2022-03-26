class Solution:
    def compareWord(self, s1, s2):
        for i in range(min(len(s1), len(s2))):
            if s1[i] != s2[i]:
                return s1[i], s2[i]
        return None

    def getLetterList(self, words):
        letter_set = set()
        for word in words:
            for letter in word:
                letter_set.add(letter)
        return list(letter_set)

    def initLetterOrderList(self, letter_set):
        beforeOrderMap = {}
        afterOrderMap = {}
        for letter in letter_set:
            beforeOrderMap[letter] = set()
            afterOrderMap[letter] = set()
        return beforeOrderMap, afterOrderMap

    def alien_order(self, words):
        letter_list = self.getLetterList(words)
        beforeOrderMap, afterOrderMap = self.initLetterOrderList(letter_list)
        for i in range(len(words) - 1):
            compare = self.compareWord(words[i], words[i + 1])
            if compare is not None:
                beforeOrderMap[compare[1]] = compare[0]
                afterOrderMap[compare[0]] = compare[1]
        print("beforeOrderMap: ", beforeOrderMap)
        print("=======================================")
        print("afterOrderMap: ", afterOrderMap)


if __name__ == '__main__':
    ls = [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]
    solution = Solution()

    result = solution.alien_order(ls)
    # print("result = ", result)
