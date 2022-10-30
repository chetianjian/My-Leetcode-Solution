# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
# 每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。
# 请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
#
#
#  示例 1：
# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
#
#
#  示例 2：
# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
#
#
#  提示：
#  2 <= cost.length <= 1000
#  0 <= cost[i] <= 999


def minCostClimbingStairs(cost: list[int]) -> int:
    if len(cost) < 2:
        return 0
    else:
        return min(minCostClimbingStairs(cost[:-1]) + cost[-1],
                   minCostClimbingStairs(cost[:-2]) + cost[-2])


def minCost_dp(cost: list[int]) -> int:
    if len(cost) < 2:
        return 0
    else:
        dp = [0, 0]  # dp[i] 为爬上第 i 层所需的最少体力
        for j in range(2, len(cost)+1):  # len(cost) + 1 表示要上到顶楼
            dp.append(min(cost[j-1] + dp[j-1], cost[j-2] + dp[j-2]))
        return dp[-1]

print(minCostClimbingStairs([10, 15, 20]))
print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minCostClimbingStairs([0, 1, 1, 1]))
print(minCostClimbingStairs([0, 1, 1, 0]))

print(minCost_dp([10, 15, 20]))
print(minCost_dp([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(minCost_dp([0, 1, 1, 1]))
print(minCost_dp([0, 1, 1, 0]))