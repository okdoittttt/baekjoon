import sys
'''
골드5: 친구 관계 파악하기
'''
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
N, M = map(int, input().split())

flg = False
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)


def DFS(cur, depth):
    global flg
    if depth == 5:
        flg = True
        return

    visited[cur] = True
    for i in A[cur]:
        if not visited[i]:
            DFS(i, depth+1)
    visited[cur] = False


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)


for i in range(N):
    DFS(i, 1)
    if flg:
        break

if flg:
    print(1)
else:
    print(0)