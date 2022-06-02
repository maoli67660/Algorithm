'''
Leetcode 14. 最长公共前缀
难度， 简单

最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""

https://leetcode-cn.com/problems/longest-common-prefix/

使用方法二，reduce，在leetcode提交超时
'''
from typing import List

def longestCommonPrefix(self, strs: List[str]) -> str:
    rst = []
    for ch in zip(*strs):
        if len(set(ch))==1:
            rst.append(ch[0])
        else:
            break
    return ''.join(rst)


if __name__ == '__main__':
    assert longestCommonPrefix_1(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix_1(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix_1(["aaa", "aaa", "aa"]) == "aa"

    assert longestCommonPrefix_2(["flower", "flow", "flight"]) == "fl"
    assert longestCommonPrefix_2(["dog", "racecar", "car"]) == ""
    assert longestCommonPrefix_2(["aaa", "aaa", "aa"]) == "aa"

    print('-----')
