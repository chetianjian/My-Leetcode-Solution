import numpy as np

def islandPerimeter(grid):
    grid = np.array(grid)

    grid = np.insert(grid, [0, grid.shape[0]], values=[0] * grid.shape[1], axis=0)
    grid = np.insert(grid, 0, values=[0] * grid.shape[0], axis=1)
    grid = np.insert(grid, grid.shape[1], values=[0] * grid.shape[0], axis=1)

    location = [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i, j] == 1 and
                sum([grid[i + 1, j], grid[i - 1, j], grid[i, j + 1], grid[i, j - 1]]) != 4]

    return len([(location[k][0]+i, location[k][1]) for k in range(len(location)) for i in [-1, 1]
                    if grid[location[k][0]+i, location[k][1]] == 0] + \
               [(location[k][0], location[k][1]+j) for k in range(len(location)) for j in [-1, 1]
                    if grid[location[k][0], location[k][1]+j] == 0])

a = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
print(islandPerimeter(a))
