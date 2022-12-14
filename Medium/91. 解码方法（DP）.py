# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：
#
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
#
#  要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为：
#  "AAJF" ，将消息分组为 (1 1 10 6)
#  "KJF" ，将消息分组为 (11 10 6)
#
#  注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。
#  给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。
#  题目数据保证答案肯定是一个 32 位 的整数。
#
#
#  示例 1：
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#
#  示例 2：
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#
#  示例 3：
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#
#
#  提示：
#  1 <= s.length <= 100
#  s 只包含数字，并且可能包含前导零。


def numDecodings(s: str) -> int:
    if s[0] == "0":
        return 0
    else:
        dp = [1]  # 设 dp[i] 为 s[: i+1] （到 s[i] 处）对应的解码方法数量。
        for i in range(1, len(s)):
            # 最后两位数同时为 0，没有对应的解码方法，返回 0
            if s[i-1: i+1] == "00":
                return 0
            # 倒数第二位数为 0，表示最后一位数必须单独映射，并且倒数第三位、倒数第二位为一个两位数整体进行映射
            elif s[i-1] == "0":
                dp.append(dp[i-3])
            # 最后两位数都不为 0，且 <= 26，说明既可以把最后两位数视作一个整体，也可以分别视作个位数进行映射
            elif s[i] != "0" and int(s[i-1: i+1]) <= 26:
                dp.append(dp[i-1]+dp[i-2])
            # 倒数第二位数不为 0，最后一位数为 0，但最后两位数 <= 26，说明最后两位数只能视作一个整体进行映射
            elif s[i] == "0" and int(s[i-1: i+1]) <= 26:
                dp.append(dp[i-2])
            # 最后两位数都不为 0 且 > 26，说明最后一位数只能视作个位数进行映射
            elif s[i] != "0" and int(s[i-1: i+1]) > 26:
                dp.append(dp[i-1])
            # 倒数第二位数不为 0，最后一位数为 0，且最后两位数 > 26，没有对应的解码方法，返回 0
            else:
                return 0
    return dp[-1]


print(numDecodings("12"))
print(numDecodings("120"))
print(numDecodings("121"))
print(numDecodings("1201"))
print(numDecodings("12012"))
print(numDecodings("120139"))
print(numDecodings("1201234"))
print(numDecodings("10011"))