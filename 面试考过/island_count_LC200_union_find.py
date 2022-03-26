import numpy as np

def find(x, parent):
    while x!= parent[x]:
        x = parent[x]
    return x

def union(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x > y:
        parent[x] = y
    else: 
        parent[y] = x

def count_island(grid):
    cols = len(grid[0])
    rows = len(grid)
    parent = list(range(cols*rows))

    for i in range(rows):
        for j in range(cols):
            encode = i * cols + j
            right = encode + 1            # 右边
            down = encode + cols          # 下边
            if j + 1 < cols and grid[i][j] == grid[i][j+1]:
                union(encode, right, parent)
            if i + 1 < rows and grid[i][j] == grid[i+1][j]:
                union(encode, down, parent)
    count = 0
    for i in range(rows*cols):
        if parent[i]==i and grid[int(i/cols)][i%cols]==1:
            count+= 1
    return count
