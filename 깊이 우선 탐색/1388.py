from sys import stdin
'''
실버4: 바닥 장식
'''
N, M = map(int, stdin.readline().split())
A = []

for _ in range(N):
    A.append(list(stdin.readline()))


def DFS(x, y):
    if A[x][y] == '-':
        A[x][y] = 1
        for a in [1, -1]:
            Y = y + a
            if (0 < Y < M) and A[x][Y] == '-':
                DFS(x, Y)

    if A[x][y] == '|':
        A[x][y] = 1
        for b in [1, -1]:
            X = x + b
            if (0 < X < N) and A[X][y] == '|':
                DFS(X, y)


count = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == '-' or A[i][j] == '|':
            DFS(i, j)
            count += 1

print(count)