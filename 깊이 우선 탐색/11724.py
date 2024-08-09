import sys
'''
실버2: 연결 요소의 개수

1. 그래프를 인접 리스트로 저장하고 방문 리스트도 초기화한다.
방향이 없기 때문에 양쪽 방향으로 에지를 모두 저장한다.

2. 임의의 시작점에서 DFS를 시작한다.

3. 아직 방문하지 않은 노드가 있을 때 시작점을 다시 정해 탐색을 진행한다.

4. 1~3 과정을 통해 총 몇 번의 DFS가 진행되는지 확인한다.

*재귀 문제 풀 때 팁*
sys.setrecursionlimit()
재귀 문제를 풀 때 런타임 에러를 예방할 수 있는 함수. 재귀의 최대 깊이를 설정한다.
만약 매개변수로 (10 ** 4) 만큼을 설정하면 호출 깊이를 10000으로 설정할 수 있다.
'''
sys.setrecursionlimit(10 ** 4)
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]    # 인접 리스트를 나타내는 2차원 리스트를 초기화
visited = [False] * (N+1)       # 노드의 방문 여부를 나타내는 리스트를 초기화


def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, N+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
