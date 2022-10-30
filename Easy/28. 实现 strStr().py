# 实现strStr()函数。
# 给你两个字符串haystack和needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回-1。

# 输入：haystack = "hello", needle = "ll"
# 输出：2

def strStr(haystack, needle):
    return haystack.find(needle)