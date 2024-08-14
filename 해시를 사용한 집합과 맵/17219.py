import sys
'''
실버4: 비밀번호 찾기
'''
input = sys.stdin.readline

N, M = map(int, input().split())

D = dict()
for _ in range(N):
    site, pwd = input().rstrip().split()
    D[site] = pwd

for _ in range(M):
    print(D[input().rstrip()])