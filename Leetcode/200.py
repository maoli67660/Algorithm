def numIslands(grid):
    num_col = len(grid[0])
    num_row = len(grid)
    count = 0
    visited = []
    for i in range(num_row):
        visited.append([False] * num_col)

    for col in range(num_col):
        for row in range(num_row):
            if not visited[row][col] and grid[row][col] == '1':
                BFS((row, col), grid, visited)
                count = count + 1
    return count


def BFS(vertex, grid, visited):
    queue = [vertex]

    while queue:
        row, col = queue.pop(0)
        if row - 1 >= 0 and grid[row - 1][col] == '1' and not visited[row - 1][col]:
            queue.append((row - 1, col))
            visited[row - 1][col] = True
        if row + 1 <= len(grid) - 1 and grid[row + 1][col] == '1' and (not visited[row + 1][col]):
            queue.append((row + 1, col))
            visited[row + 1][col] = True
        if col - 1 >= 0 and grid[row][col - 1] == '1' and not visited[row][col - 1]:
            queue.append((row, col - 1))
            visited[row][col - 1] = True
        if col + 1 <= len(grid[0]) - 1 and grid[row][col + 1] == '1' and not visited[row][col + 1]:
            queue.append((row, col + 1))
            visited[row][col + 1] = True


if __name__ == '__main__':
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print('Reult', numIslands(grid))
