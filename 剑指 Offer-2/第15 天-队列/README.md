# 剑指 Offer-第二部
https://leetcode-cn.com/study-plan/lcof/?progress=06polim

### 第 15 天 队列
##### 树的层次遍历
```python
def level_order(root):
    queue = [root]
    level_num = 1
    res = []
    while queue:
        level_count = 0
        level_ls = []
        for _ in range(level_num):
            top = queue.pop(0)
            level_ls.append(top.val)
            if top.left:
                queue.append(top.left)
                level_count+=1
            if top.right:
                queue.append(top.right)
                level_count+=1
        level_num = level_count
        res.append(level_ls)
    return res
```

* 剑指 Offer II 044. 二叉树每层的最大值 (树,深度优先搜索,广度优先搜索,二叉树,中等,通过率 63.5%)
* 剑指 Offer II 045. 二叉树最底层最左边的值 (树,深度优先搜索,广度优先搜索,二叉树,中等,通过率 80.2%)
* 剑指 Offer II 046. 二叉树的右侧视图 (树,深度优先搜索,广度优先搜索,二叉树,中等,通过率 71.8%)
