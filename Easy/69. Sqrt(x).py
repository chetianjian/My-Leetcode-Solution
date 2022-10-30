# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被舍去 。
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5。

# 示例 1：
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

def mySqrt(x):
    import math

    def h(h):
        h = int(math.ceil(h))
        if h * h < x:
            return int(math.floor(h)) + 1
        elif h * h == x:
            return int(math.floor(h))
        elif h * h > x:
            return int(math.floor(h)) - 1

    L, R = 0, x
    for i in range(0, 50):
        mid = (L + R) / 2
        if mid * mid > x:
            R = mid
            if mid - L < 10e-10:
                return h(mid)
        elif mid * mid == x:
            return h(mid)
        elif mid * mid < x:
            L = mid
            if R - mid < 10e-8:
                return h(R)
    return h(max(L, R, mid))

