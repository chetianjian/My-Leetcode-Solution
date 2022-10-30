# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#
#  注意：
#  一个有效的数独（部分已被填充）不一定是可解的。
#  只需要根据以上规则，验证已经填入的数字是否有效即可。
#  空白格用 '.' 表示。
#
#
#  示例 1：
# 输入：board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：true
#
#
#  示例 2：
# 输入：board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# 输出：false
# 解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无
# 效的。
#
#
# 提示：
#  board.length == 9
#  board[i].length == 9
#  board[i][j] 是一位数字（1-9）或者 '.'

import numpy as np


# 我的第一解法：
def isValidSudoku(board):
    board = np.array(board)
    for i in range(9):
        row_data, col_data = [m for m in board[i, :] if m != "."], [n for n in board[:, i] if n != "."]
        if len(row_data) != len(set(row_data)) or len(col_data) != len(set(col_data)):
            return False
        else:
            continue

    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            sub_board = []
            for i in range(3):
                i = i + k
                for j in range(3):
                    j = j + l
                    sub_board.append(board[i, j])
            sub_board = [h for h in sub_board if h != "."]
            if len(sub_board) != len(set(sub_board)):
                return False
            else:
                continue
    return True


print(isValidSudoku(board=[["8", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                           [".", "9", "8", ".", ".", ".", ".", "6", "."],
                           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                           [".", "6", ".", ".", ".", ".", "2", "8", "."],
                           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                     [".", "4", ".", "3", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                     ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                     [".", ".", "2", ".", "7", ".", ".", ".", "."],
                     [".", "1", "5", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", "2", ".", ".", "."],
                     [".", "2", ".", "9", ".", ".", ".", ".", "."],
                     [".", ".", "4", ".", ".", ".", ".", ".", "."]]))


# 我的第二解法：
def isValidSudoku1(board):
    board = np.array(board)
    for i in range(9):
        dic1, dic2 = {"default":0}, {"default":0}
        for item in range(9):
            dic1[board[i, item]] = dic1.get(board[i, item], 0) + 1
            dic2[board[item, i]] = dic2.get(board[item, i], 0) + 1
        if "." in dic1: del dic1["."]
        if "." in dic2: del dic2["."]
        if max(dic1.values()) > 1 or max(dic2.values()) > 1:
            return False

    for k in [0, 3, 6]:
        for l in [0, 3, 6]:
            dic1 = {"default": 0}
            for i in range(3):
                i = i + k
                for j in range(3):
                    j = j + l
                    dic1[board[i, j]] = dic1.get(board[i, j], 0) + 1
            if "." in dic1: del dic1["."]
            if max(dic1.values()) > 1:
                return False

    return True


print(isValidSudoku1(board=[["8", "3", ".", ".", "7", ".", ".", ".", "."],
                            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                            [".", "9", "8", ".", ".", ".", ".", "6", "."],
                            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                            [".", "6", ".", ".", ".", ".", "2", "8", "."],
                            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku1(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."],
                            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                            [".", "9", "8", ".", ".", ".", ".", "6", "."],
                            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                            [".", "6", ".", ".", ".", ".", "2", "8", "."],
                            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku1([[".", ".", ".", ".", "5", ".", ".", "1", "."],
                      [".", "4", ".", "3", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "3", ".", ".", "1"],
                      ["8", ".", ".", ".", ".", ".", ".", "2", "."],
                      [".", ".", "2", ".", "7", ".", ".", ".", "."],
                      [".", "1", "5", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", "2", ".", ".", "."],
                      [".", "2", ".", "9", ".", ".", ".", ".", "."],
                      [".", ".", "4", ".", ".", ".", ".", ".", "."]]))

print(isValidSudoku1([[".",".",".",".",".",".",".",".","."],
                      ["8",".",".",".",".","7",".",".","."],
                      [".",".",".","8",".",".",".",".","."],
                      [".",".",".",".","9",".","2",".","5"],
                      ["8",".",".",".",".",".",".",".","."],
                      [".",".",".",".",".",".",".",".","."],
                      [".","3",".",".","6",".",".",".","."],
                      [".",".",".",".",".",".",".","8","."],
                      [".",".","9",".",".",".",".",".","."]]))