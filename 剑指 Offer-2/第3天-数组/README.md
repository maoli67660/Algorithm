# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 3 天 数组
* 剑指 Offer II 007. 数组中和为 0 的三个数 (数组,双指针,排序,中等,通过率 44.7%)
> 先排序。  遍历 i 0~len(nums)-2    对每个循环 left = i+1, right = len-1 双指针搜索。  难点，rst先用set除重， 如果搜索到，left right同时挪动，继续向里搜索。
* 剑指 Offer II 008. 和大于等于 target 的最短子数组 (数组,二分查找,前缀和,滑动窗口,中等,通过率 49.3%)
> 前缀和（别忘s0=0）通向双指针。 搜索失败标记0判断。 注意len(nums)=1 情况是否包括。
* 剑指 Offer II 009. 乘积小于 K 的子数组 (数组,滑动窗口,中等,通过率 54.4%)
