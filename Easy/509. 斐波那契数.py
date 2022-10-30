# 斐波那契数，通常用F(n) 表示，形成的序列称为 斐波那契数列 。该数列由0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
# 给你 n ，请计算 F(n) 。

# 示例：
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3


# 递归
def fib(n):
    if n <= 1: return n
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    count, a, b = 1, 0, 1
    if n == 0:
        return 0
    while count < n:
        a, b = b, a + b
        count = count + 1
    return b