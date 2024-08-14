import sys
'''
실버3: 바이러스
'''
N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def DFS(V):
    visited[V] = 1
    for next in graph[V]:
        if not visited[next]:
            DFS(next)


DFS(1)
print(sum(visited)-1)
