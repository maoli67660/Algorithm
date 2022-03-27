# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 2 天 整数
* 剑指 Offer II 004. 只出现一次的数字 (位运算,数组,中等,通过率 71.0%)
> return [key for key , val in Counter(nums).items() if val == 1][0]
* 剑指 Offer II 005. 单词长度的最大乘积 (位运算,数组,字符串,中等,通过率 70.5%)
> 两层循环， 便利所有word。  如果 set(word[i]) & set(word[j]) == set() 比较最大值
* 剑指 Offer II 006. 排序数组中两个数字之和 (数组,双指针,二分查找,简单,通过率 64.5%)
> left, right = 0, len-1.  大于target right-1 小于target left+1 最后return [left, right]
