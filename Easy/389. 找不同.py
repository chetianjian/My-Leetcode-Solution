# 给定两个字符串 s 和 t，它们只包含小写字母。
# 字符串t由字符串s随机重排，然后在随机位置添加一个字母。
# 请找出在 t 中被添加的字母。

# 示例 1：
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。

def findTheDifference(s, t):
    t = list(t)
    for i in s:
        t.remove(i)
    return t[0]

# 解题思路: 首先将两个字符串合并为a, 在a中遍历，如果出现奇数次的字符即为不同的字符。

def findTheDifference1(s, t):
    a = "".join([s, t])
    for ch in a:
        if a.count(ch) % 2 == 1:
            return ch