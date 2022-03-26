# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 23 天 二分查找 ->熟悉bisect包
* 剑指 Offer II 068. 查找插入位置 (数组,二分查找,简单,通过率 50.1%)
> 二分法
* 剑指 Offer II 069. 山峰数组的顶部 (数组,二分查找,简单,通过率 71.5%)
* 剑指 Offer II 070. 排序数组中只出现一次的数字 (数组,二分查找,中等,通过率 65.0%)
> 二分法变种。 如果相邻数值相同，通过下标检查该数字是否出现过。  
> 懒人方法 O(n)
```python
return [kv[0] for kv in Counter(nums).items() if kv[1]==1][0]
```
