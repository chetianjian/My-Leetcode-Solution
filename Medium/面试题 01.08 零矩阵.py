# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。 
# 
#  示例 1： 
#  输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#  
#  示例 2： 
#  输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    position = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                position.append((i, j))
    for pos in position:
        row, col = pos[0], pos[1]
        for i in range(len(matrix)):
            matrix[i][col] = 0
        for j in range(len(matrix[0])):
            matrix[row][j] = 0
    return matrix

print(setZeroes([[0,1,2,0], [3,4,5,2], [1,3,1,5]]))