import sys
'''
실버2: DFS와 BFS
tip: DFS, BFS 문제를 풀 때는 거의 visitied 리스트가 필요하다. 이를 염두하고 문제를 풀 것.
BFS에는 Queue가 필요한 경우가 많다.
'''
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def DFS(idx):
    global visited
    visited[idx] = True
    print(idx, end=' ')
    for i in range(1, (N + 1)):
        if not visited[i] and graph[idx][i]:
            DFS(i)


def BFS():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for i in range(1, (N + 1)):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                q.append(i)


DFS(V)
print()

visited = [False] * (N + 1)
q = [V]
visited[V] = True
BFS()
print()
