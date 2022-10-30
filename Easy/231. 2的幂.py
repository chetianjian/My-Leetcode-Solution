# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

# 如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

# 示例
# 输入：n = 16
# 输出：true
# 解释：24 = 16

# 示例
# 输入：n = 3
# 输出：false

def isPowerOfTwo(n):
    L = -1
    if n < 1: return False
    while 2 ** L < n:
        if 2 ** (L + 1) > n:
            return False
        elif 2 ** (L + 1) < n:
            L = L + 1
        else:
            return True

def isPowerOfTwo2(n):
    lst = [2**i for i in range(0, 31)]
    if n in lst:
        return True
    else:
        return False

def isPowerOfTwo3(n):
    if n == 1:
        return True
    if n < 1 or n%2 == 1:
        return False
    if n > 1:
        return isPowerOfTwo3(n/2)