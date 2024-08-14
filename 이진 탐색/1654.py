from sys import stdin
'''
실버2: 랜선 자르기
'''
K, N = map(int, input().split())
LAN = [int(stdin.readline()) for _ in range(K)]
start, end = 1, max(LAN)

while start <= end:
    midi = (start + end) // 2
    lines = 0

    for i in LAN:
        lines += i // midi

    if lines >= N:
        start = midi + 1
    else:
        end = midi -1

print(end)