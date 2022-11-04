# 给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母
# 。如果不存在这样的两个单词，返回 0 。
#
#
#  示例 1：
# 输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出：16
# 解释：这两个单词为 "abcw", "xtfn"。
#
#  示例 2：
# 输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
# 输出：4
# 解释：这两个单词为 "ab", "cd"。
#
#  示例 3：
# 输入：words = ["a","aa","aaa","aaaa"]
# 输出：0
# 解释：不存在这样的两个单词。
#
#
#  提示：
#  2 <= words.length <= 1000
#  1 <= words[i].length <= 1000
#  words[i] 仅包含小写字母


def maxProduct(words: list[str]) -> int:
    from itertools import combinations
    words = sorted(words, key=lambda w: len(w), reverse=True)
    iterator = iter(combinations(words, 2))
    highest = 0
    try:
        while True:
            comb = next(iterator)
            if len(set(comb[0]) | set(comb[1])) < len(set(comb[0])) + len(set(comb[1])):
                continue
            elif len(comb[0]) * len(comb[1]) > highest:
                highest = len(comb[0]) * len(comb[1])
    except:
        return highest
    return highest


print(maxProduct(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(maxProduct(words=["a", "aa", "aaa", "aaaa"]))
print(maxProduct(words=["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]))
print(maxProduct(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))


def maxProduct1(words: list[str]) -> int:
    from itertools import combinations
    words = sorted(words, key=lambda w: len(w), reverse=True)
    lst = list(combinations(words, 2))

    def product(comb):
        if len(set(comb[0]) | set(comb[1])) < len(set(comb[0])) + len(set(comb[1])):
            return 0
        else:
            return len(comb[0]) * len(comb[1])

    return max(map(product, lst))


print(maxProduct1(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(maxProduct1(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(maxProduct1(words=["a", "aa", "aaa", "aaaa"]))
print(maxProduct1(words=["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]))
print(maxProduct1(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))


def maxProduct2(words: list[str]) -> int:
    word_sets = [set(w) for w in words]
    result = 0
    for i, j in enumerate(words):
        for w in range(i + 1, len(words)):
            if not word_sets[i] & word_sets[w]:
                result = max(result, len(j) * len(words[w]))
    return result


print(maxProduct2(words=["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
print(maxProduct2(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
print(maxProduct2(words=["a", "aa", "aaa", "aaaa"]))
print(maxProduct2(words=["eae", "ea", "aaf", "bda", "fcf", "dc", "ac", "ce", "cefde", "dabae"]))
print(maxProduct2(words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
