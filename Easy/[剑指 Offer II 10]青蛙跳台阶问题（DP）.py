# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。q
#
#  示例 1：
#  输入：n = 2
# 输出：2
#
#  示例 2：
#  输入：n = 7
# 输出：21
#
#  示例 3：
#  输入：n = 0
# 输出：1
#
#  提示：
#  0 <= n <= 100

def numWays(n: int) -> int:
    if n <= 1:
        return 1
    else:
        return numWays(n-1) + numWays(n-2)
print(numWays(7))

########################################################################################

def numWays_modified(n: int) -> int:
    if n <= 1:
        return 1
    else:
        dp = [1, 1]
        for i in range(n - 2):
            dp.append(dp[-2] + dp[-1])
        return dp[-2] + dp[-1]

print(numWays_modified(7))

########################################################################################

def numWays_inplace(n: int) -> int:
    if n <= 1:
        return 1
    else:
        i, j = 1, 1
        for iter in range(n-1):
            i, j = j, i+j
        return j

print(numWays_inplace(7))




