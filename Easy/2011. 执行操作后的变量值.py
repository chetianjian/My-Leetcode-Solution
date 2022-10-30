# 存在一种仅支持 4 种操作和 1 个变量 X 的编程语言：
# ++X 和 X++ 使变量 X 的值 加 1
# --X 和 X-- 使变量 X 的值 减 1
# 最初，X 的值是 0
# 给你一个字符串数组 operations ，这是由操作组成的一个列表，返回执行所有操作后， X 的 最终值 。

# 示例 1：
# 输入：operations = ["--X","X++","X++"]
# 输出：1
# 解释：操作按下述步骤执行：
# 最初，X = 0
# --X：X 减 1 ，X =  0 - 1 = -1
# X++：X 加 1 ，X = -1 + 1 =  0
# X++：X 加 1 ，X =  0 + 1 =  1

def finalValueAfterOperations(operations):
    dic = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
    return sum([dic.get(i) for i in operations])


print(finalValueAfterOperations(["X++", "++X", "--X", "X--"]))
