class Solution:
    def isAlienSorted(self, words, order):
        alien_dict = {}
        for index, char in enumerate(order):
            alien_dict[char] = index

        def compare_word(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    if alien_dict[w1[i]] < alien_dict[w2[i]]:
                        return True
                    else:
                        return False
            return len(w1) < len(w2)

        flag = True
        for i in range(len(words) - 1):
            flag = flag and compare_word(words[i], words[+ 1])
            if not flag:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    words = ["apple", "app"]
    order = 'abcdefghijklmnopqrstuvwxyz'
    result = solution.isAlienSorted(words, order)
    print('result : ', result)
