import numpy as np

def dfs(i, matrix):
    for j in matrix[i,:]:
        if matrix[i,j] == 1:
            matrix[i,j] = 0
            dfs(j,matrix)
            
def bfs(i, matrix):
    queue = [i]
    while queue:
        top = queue.pop(0)
        for n in matrix[top]:
            if matrix[top,n] == 1:
                matrix[top,n] = 0
                queue.append(n)
                
                
def count_graphs(matrix, visit_func):
    N = len(matrix)
    count = 0
    for i in range(N):
            if matrix[i,i] == 1:
                count+=1
                visit_func(i, matrix)
    return count
    
    
if __name__ == '__main__':
    mat = np.array([[1,0,0,0],
                [0,1,1,0],
                [0,1,1,0],
                [1,0,0,1]])
    
    print('count graph via DFS', count_graphs(mat.copy(), dfs))
    print('count graph via BFS', count_graphs(mat.copy(), bfs))
