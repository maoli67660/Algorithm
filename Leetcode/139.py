class Solution:
    def wordBreak(self, s, wordDict):
        def preprocss_dic():
            del_ls = set()
            s_set = set(s)
            for word in wordDict:
                if s_set | set(word) != s_set:
                    del_ls.add(word)
            print('preprocss_dic    del_ls = ', del_ls)
            for item in del_ls:
                wordDict.remove(item)

            wordDict.sort(key=lambda x: len(x))
            del_ls = set()
            for i in range(len(wordDict)):
                for j in range(i + 1, len(wordDict)):
                    if len(wordDict[j]) / len(wordDict[i]) == int(len(wordDict[j]) / len(wordDict[i])):
                        if int(len(wordDict[j]) / len(wordDict[i])) * wordDict[i] == wordDict[j]:
                            del_ls.add(wordDict[j])
            for item in del_ls:
                wordDict.remove(item)
            return wordDict

        def myWordBreak(s):
            valid_sub_words = []
            for word in wordDict:
                if word == s:
                    return True
                if s[:len(word)] == word:
                    valid_sub_words.append(s[len(word):])

            if len(valid_sub_words) == 0:
                return False
            else:
                for sub_word in valid_sub_words:
                    if myWordBreak(sub_word):
                        return True
                return False

        wordDict = preprocss_dic()
        print('wordDict', wordDict)
        return myWordBreak(s)


if __name__ == '__main__':
    solution = Solution()

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

    wordDict = ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa", "ba"]


    result = solution.wordBreak(s, wordDict)
    # print("result = ", result)

    # def preprocss_dic():
    #     del_ls = set()
    #     s_set = set(s)
    #     for word in wordDict:
    #         if s_set | set(word) != s_set:
    #             del_ls.add(word)
    #     print('preprocss_dic    del_ls = ', del_ls)
    #     for item in del_ls:
    #         wordDict.remove(item)
    #
    #     wordDict.sort(key=lambda x: len(x))
    #     del_ls = set()
    #     for i in range(len(wordDict)):
    #         for j in range(i + 1, len(wordDict)):
    #             if len(wordDict[j]) / len(wordDict[i]) == int(len(wordDict[j]) / len(wordDict[i])):
    #                 if int(len(wordDict[j]) / len(wordDict[i])) * wordDict[i] == wordDict[j]:
    #                     del_ls.add(wordDict[j])
    #     print('@preprocss_dic    del_ls = ', del_ls)
    #     for item in del_ls:
    #         wordDict.remove(item)
    #     return wordDict
    #
    # print('preprocss_dic: ', preprocss_dic())
