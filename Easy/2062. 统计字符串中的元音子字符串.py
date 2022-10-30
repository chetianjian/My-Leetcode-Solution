# 子字符串 是字符串中的一个连续（非空）的字符序列。
# 元音子字符串 是 仅 由元音（'a'、'e'、'i'、'o' 和 'u'）组成的一个子字符串，且必须包含 全部五种 元音。
# 给你一个字符串 word ，统计并返回 word 中 元音子字符串的数目 。

def countVowelSubstrings(word):
    import re
    count = 0

    def ismorethanfive(x):
        return len(set(x)) >= 5

    for item in filter(ismorethanfive, re.findall("[aeiou]{5,}", word)):
        i = 0
        while i <= len(item) - 5:
            j = i + 4
            while j <= len(item):
                if len(set(item[i:j])) == 5:
                    count += 1
                j += 1
            i += 1
    return count

print(countVowelSubstrings("cuaieuouac"))