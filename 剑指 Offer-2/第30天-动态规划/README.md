# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim


### 第 30 天 动态规划 ->重要
* 剑指 Offer II 088. 爬楼梯的最少成本 (数组,动态规划,简单,通过率 73.9%)
> dp[i] = max(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
* 剑指 Offer II 089. 房屋偷盗 (数组,动态规划,中等,通过率 61.4%)
> dp[i] = max(dp[i-1], dp[i-2] + nums[i])
* 剑指 Offer II 090. 环形房屋偷盗 (数组,动态规划,中等,通过率 49.5%)
> 上题做两次  一次不含尾 nums[:-1] 一次不含头 nums[1:] 

