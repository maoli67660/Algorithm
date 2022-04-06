# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 1 天 整数
* 剑指 Offer II 001. 整数除法 (位运算,数学,简单,通过率 20.8%)

给定两个整数 a 和 b ，求它们的除法的商 a/b ，要求不得使用乘号 '*'、除号 '/' 以及求余符号 '%' 。

思路： 用减法 不断执行 b-a. 优化： a = a+a 推动时间复杂度往 O(log n)

* 剑指 Offer II 002. 二进制加法 (位运算,数学,字符串,模拟,简单,通过率 55.8%)
* 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数 (位运算,动态规划,简单,通过率 78.6%)

```python
def countOnes(x: int) -> int:
    ones = 0
    while x > 0:
        x &= (x - 1)
        ones += 1
    return ones

def countBits(self, n: int) -> List[int]:
    return [countOnes(i) for i in range(n + 1)]
```
