# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 true ；否则，返回 false 。
# 整数 n 是 3 的幂次方需满足：存在整数 x 使得 n == 3x

# 示例 1：
# 输入：n = 27
# 输出：true


# 递归
def isPowerOfThree(n):
    if str(n)[-1] not in ["1", "3", "9", "7"]:
        return False
    def power3(n):
        if n == 1:
            return True
        return power3(n / 3) if n > 1 else False
    return power3(n)


def isPowerOfThree2(n):
    return True if n in [3**i for i in range(0, 31)] else False


def isPowerOfThree3(n) -> bool:
    while n >= 1:
        if n == 1: return True
        n = n / 3
    return False