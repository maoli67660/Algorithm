# K queens problem
from copy import deepcopy
def check(A,i,j):
    for k in range(0,i):
        if A[k][j] == 'X':
            return False
            
    for k in range(min(i,j)+1):
        if A[i-k][j-k] == 'X':
            return False
    for k in range(min(i+1,len(A)-j)):
        if A[i-k][j+k] == 'X':
            return False
    return True

def dfs(A,i, rst):
    for j in range(0,len(A)):
        if check(A,i,j):
            A[i][j] = 'X'
            dfs(A,i+1,rst)
            if i == len(A)-1:
                rst.append(deepcopy(A))
            A[i][j] = 'o'

def printM(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], ' ', end='')
        print()
    print('+' * 20)


if __name__ == '__main__':
    print('------------------')
    A4 = [['o','o','o','o'],
         ['o','o','o','o'],
         ['o','o','o','o'],
         ['o','o','o','o']]
         
    A8 = [['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o'],
         ['o','o','o','o','o','o','o','o']]

    rst = []
    dfs(A4,0,rst)
    for i in range(len(rst)):
        printM(rst[i])
