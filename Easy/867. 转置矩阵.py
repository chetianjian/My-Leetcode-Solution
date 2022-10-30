def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

print(transpose([[1,2,3],[4,5,6]]))