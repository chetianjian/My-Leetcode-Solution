# 给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

# 有效字符串需满足：
# 1. 左括号必须用相同类型的右括号闭合。
# 2. 左括号必须以正确的顺序闭合。

def isValid(s):
    lst = list(s)
    previous, now = len(lst), len(lst) - 1

    while now < previous:
        previous = now
        for i in range(0, len(lst) - 1):
            if lst[i] + lst[i + 1] in ["()", "[]", "{}"]:
                lst[i], lst[i + 1] = "0", "0"
        for j in range(len(lst) - 1, -1, -1):
            if lst[j] == "0": lst.pop(j)
        if len(lst) == 0:
            return True
        else:
            now = len(lst)
    return False
