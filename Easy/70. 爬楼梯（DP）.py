# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 注意：给定 n 是一个正整数。

# 递归
def climbStairs(n):
    if n <= 3: return n
    return climbStairs(n - 1) + climbStairs(n - 2)


print(climbStairs(44))


def fib2(n):
    count, a, b = 1, 1, 1
    if n == 0:
        return 0
    while count < n:
        a, b = b, a + b
        count = count + 1
    return b


print(fib2(6))


