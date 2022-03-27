# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 5 天  字符串
* 剑指 Offer II 014. 字符串中的变位词 (哈希表,双指针,字符串,滑动窗口,中等,通过率 51.3%)
> Counter(s1) 是否等于滑动窗口 Counter(s2[i：i+win_size])
* 剑指 Offer II 015. 字符串中的所有变位词 (哈希表,字符串,滑动窗口,中等,通过率 62.5%)
> 同上，检查滑动窗口counter和目标count是否一致
* 剑指 Offer II 016. 不含重复字符的最长子字符串 (哈希表,字符串,滑动窗口,中等,通过率 48.1%)
> 用dict记录访问的字符和其index。如果没访问过，则更新计数器并继续往前走。 如果访问过，回退到重复字符的下一个字符开始，dict清空。
