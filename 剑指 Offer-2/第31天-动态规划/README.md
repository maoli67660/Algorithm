# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim


### 第 31 天  动态规划 ->重要
* 剑指 Offer II 091. 粉刷房子 (数组,动态规划,中等,通过率 77.4%)
>典型多维状态动态规划。 值得参考
```python
def minCost(costs):
    dp = [[float('inf')]*3 for i in range(len(costs))]
    dp[0][0], dp[0][1], dp[0][2] = costs[0][0], costs[0][1], costs[0][2]
    
    for i in range(1, len(costs)):
        for j in range(3):
            for k in range(3):
                if k!=j:
                    dp[i][j] = min(dp[i][j], dp[i-1][k]+costs[i][j])
    return min(dp[-1])
```
* 剑指 Offer II 092. 翻转字符 (字符串,动态规划,中等,通过率 66.6%)
* 剑指 Offer II 093. 最长斐波那契数列 (数组,哈希表,动态规划,中等,通过率 58.4%)

