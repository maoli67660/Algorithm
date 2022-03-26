# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 20 天 堆
* 剑指 Offer II 059. 数据流的第 K 大数值  (树,设计,二叉搜索树,二叉树,数据流,堆（优先队列）,简单,通过率 63.6%)
* 剑指 Offer II 060. 出现频率最高的 k 个数字 (数组,哈希表,分治,桶排序,计数,快速选择,排序,堆（优先队列）,中等,通过率 68.8%)
```python
return [key_val[0] for key_val in sorted(Counter(nums).items(), key = lambda x:x[1], reverse=True)[:k]]
```
* 剑指 Offer II 061. 和最小的 k 个数对  (数组,堆（优先队列, 中等, 通过率 55.1%)
