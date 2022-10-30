# 2068. 检查两个字符串是否几乎相等
# 如果两个字符串 word1 和 word2 中从 'a' 到 'z' 每一个字母出现频率之差都 不超过 3 ，那么我们称这两个字符串 word1和word2 几乎相等 。
# 给你两个长度都为 n 的字符串 word1 和 word2 ，如果 word1 和 word2 几乎相等 ，请你返回 true ，否则返回 false 。

# 输入：word1 = "cccddabba", word2 = "babababab"
# 输出：true
# 解释：word1 和 word2 中每个字母出现频率之差至多为 3 ：
# - 'a' 在 word1 中出现了 2 次，在 word2 中出现了 4 次，差为 2 。
# - 'b' 在 word1 中出现了 2 次，在 word2 中出现了 5 次，差为 3 。
# - 'c' 在 word1 中出现了 3 次，在 word2 中出现了 0 次，差为 3 。
# - 'd' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。



def checkAlmostEquivalent(word1, word2):
    for i in set(word1):
        try:
            if abs(word1.count(i) - word2.count(i)) > 3: return False
        except:
            if word1.count(i) > 3: return False
    for i in set(word2):
        try:
            if abs(word2.count(i) - word1.count(i)) > 3: return False
        except:
            if word2.count(i) > 3: return False
    return True