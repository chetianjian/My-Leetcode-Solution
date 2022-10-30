# 猜数字游戏的规则如下：
# 每轮游戏，我都会从1到n 随机选择一个数字。 请你猜选出的是哪个数字。
# 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
# 你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1或 0）：

# -1：我选出的数字比你猜的数字小 pick < num
# 1：我选出的数字比你猜的数字大 pick > num
# 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
# 返回我选出的数字。

# 示例 1：
# 输入：n = 10, pick = 6
# 输出：6

import math
def guessNumber(n):
    L, R = 1, n

    for i in range(0, math.ceil(math.log(n, 2))):
        num = int(round((L + R) / 2 + 0.000001))
        if guess(num) == 0:
            return (num)
        elif guess(num) == -1:
            R = num
        else:
            L = num
    return int((L + R) / 2)