# 给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。
# 单词, 是指仅由字母组成、不包含任何空格字符的最大子字符串。

# 输入：s = "Hello World"
# 输出：5

def lengthOfLastWord(s):
    return len(s.split()[-1])


digits = [4,3,2,1]
digits = list(map(str, digits))

print(list("0"))