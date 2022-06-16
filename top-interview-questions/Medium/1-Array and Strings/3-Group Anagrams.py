
'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

'''
def groupAnagrams(strs):
    _dict = {}
    for s in strs:
        ss = ''.join(sorted(s))
        if ss in _dict:
            _dict[ss].append(s)
        else:
            _dict[ss] = [s]
    ls = []
    for key in _dict:
        ls.append(_dict[key])
    return ls


if __name__ == '__main__':
    strs = ['aba', 'aab', 'baa', 'cde', 'edc', 'hh']
    assert groupAnagrams(strs) == [['aba', 'aab', 'baa'], ['cde', 'edc'], ['hh']]
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    assert groupAnagrams(strs) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
