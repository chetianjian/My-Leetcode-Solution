# 给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

# 示例 1：
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

# 示例 2：
# 输入：digits = ""
# 输出：[]


def letterCombinations(digits):
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    lst = [dic[i] for i in digits]
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [i for i in lst[0]]
    elif len(lst) == 2:
        res = [i + j for i in lst[0] for j in lst[1]]
    elif len(lst) == 3:
        res = [i + j + k for i in lst[0] for j in lst[1] for k in lst[2]]
    elif len(lst) == 4:
        res = [i + j + k + l for i in lst[0] for j in lst[1] for k in lst[2] for l in lst[3]]
    return list(set(res))


# 别人的解法
def letterCombinations2(digits):
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
           "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    if len(digits) == 0:
        return []
    product = ['']
    for k in digits:
        product = [i + j for i in product for j in dic[k]]
    return product