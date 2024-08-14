'''
실버5: 듣보잡
'''
N, M = map(int, input().split())

A = set()
for _ in range(N):
    A.add(input())

B = set()
for _ in range(M):
    B.add(input())

result = sorted(list(A & B))
print(len(result))
for i in result:
    print(i)