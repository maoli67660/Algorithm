# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim


### 第 29 天 回溯法 ->重要
* 剑指 Offer II 085. 生成匹配的括号 (字符串,动态规划,回溯,中等,通过率 85.4%)
```python
def dfs(left, right, path, n ,res):
    if left==n and left==right:
        res.add(path)
        return
        
    if left >= right and left<=n:
        dfs(left+1, right, path+'(', n, res)
        dfs(left, right+1, path+')', n, res)
```
* 剑指 Offer II 086. 分割回文子字符串 (深度优先搜索,广度优先搜索,图,哈希表,中等,通过率 74.2%)
* 剑指 Offer II 087. 复原 IP (字符串,回溯,中等,通过率 63.3%)
