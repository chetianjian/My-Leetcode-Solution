# 给你两个非负整数 low 和 high 。请你返回 low 和 high 之间（包括二者）奇数的数目。
#
#  示例 1：
#  输入：low = 3, high = 7
# 输出：3
# 解释：3 到 7 之间奇数数字为 [3,5,7] 。
#
#  示例 2：
#  输入：low = 8, high = 10
# 输出：1
# 解释：8 到 10 之间奇数数字为 [9] 。
#
#
#  提示：
#  0 <= low <= high <= 10^9

import math


def countOdds(low: int, high: int) -> int:
    return int((high-low) / 2) if low % 2 == 0 and high % 2 == 0 else \
        math.floor((high-low) / 2) + 1

print(countOdds(3, 7))