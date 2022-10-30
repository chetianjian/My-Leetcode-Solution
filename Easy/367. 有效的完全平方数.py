# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 不要 使用任何内置的库函数，如 sqrt 。

# 示例 1：
# 输入：num = 16
# 输出：true

# 示例 2：
# 输入：num = 14
# 输出：false

def isPerfectSquare(num):
    a = 1
    while num > 0:
        num -= a
        a += 2
    return True if num == 0 else False