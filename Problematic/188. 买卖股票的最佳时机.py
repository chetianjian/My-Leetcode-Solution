# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
#
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
#
#
#  示例 1：
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
#
#  示例 2：
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3


#  提示：
#  0 <= k <= 100
#  0 <= prices.length <= 1000
#  0 <= prices[i] <= 1000


def maxProfit(k: int, prices: list) -> int:
    length = len(prices)
    if length == 0:
        return 0
    dp = [[0 for _ in range(length)] for _ in range(k + 1)]

    for i in range(1, k + 1):
        max_profit = -prices[0]
        for j in range(1, length):
            dp[i][j] = max(dp[i][j-1], max_profit + prices[j])
            max_profit = max(max_profit, dp[i-1][j] - prices[j])
    return dp[-1][-1]



print(maxProfit(k=2, prices=[2, 4, 1]))
print(maxProfit(k=2, prices=[3, 2, 6, 5, 0, 3]))
print(maxProfit(k=2, prices=[6, 1, 3, 2, 4, 7]))



