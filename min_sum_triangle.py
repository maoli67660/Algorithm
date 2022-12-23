'''
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示

       2
     3    4
   6   5    7
 4   1    8   4
 
minue path sum: 2+3+5+1=11

'''
def min_path_sum(arr):
    dp = copy.deepcopy(triangle)
    for x in range(1, len(triangle)):
        for y in range(len(dp[x])):
            if y == 0:
                dp[x][y] = dp[x-1][y] + triangle[x][y]
            elif y == len(dp[x])-1:
                dp[x][y] = dp[x-1][y-1] + triangle[x][y]
            else:
                dp[x][y] = min(dp[x-1][y-1], dp[x-1][y]) + triangle[x][y]

    return min(dp[-1])
  
  
  
  if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7], [4,1,8,3]]
    print('min_path_sum = ', min_path_sum(triangle))
    
