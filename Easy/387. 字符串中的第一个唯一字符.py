# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 示例：
# s = "leetcode"
# 返回 0
# s = "loveleetcode"
# 返回 2

def firstUniqChar(s):
    repeat = []
    for i in range(len(s)):
        if s[i] in repeat: continue
        if s[i] in s[i + 1:]:
            repeat.append(s[i])
            continue
        else:
            return i
    return -1