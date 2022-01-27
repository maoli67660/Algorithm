def dfs(word, board, i, j, visited):
    if (i,j) in visited or board[i][j] != word[0]:
        return False
    if len(word) == 1:
            return True
    else:
        visited.add((i,j))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            new_i = di + i
            new_j = dj + j
            if -1<new_i<len(board) and -1<new_j<len(board[0]) and dfs(word[1:], board, new_i, new_j, visited):
                    return True
        visited.remove((i,j))
        return False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(word, board, i, j, visited):
                    return True
        return False
