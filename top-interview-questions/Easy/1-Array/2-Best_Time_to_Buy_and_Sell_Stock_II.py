'''
Leetcode 122 股票买卖的最佳时间
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import numpy as np
def maxProfit(prices):
    '''
        满足局部最优解合并就是全局最优解的特点。 贪心算法。  直接计算可以产生利润的相邻时间点， 把利润累加
        Idea: prices数组的一阶差分为可能的交易利润。将其中正差分相加，即为结果。 
    '''
    diff = np.diff(np.array(prices))
    return int(diff[diff>0].sum())
# 一行过 return sum([max(prices[i]-prices[i-1],0) for i in range(1,len(prices))])

if __name__ == '__main__':
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 7  # 1-5   3-6    利润为7
    assert maxProfit([1,2,3,4,5]) == 7
    assert maxProfit([7,6,4,3,1])==0   # 没有交易， 零润为 0
    
