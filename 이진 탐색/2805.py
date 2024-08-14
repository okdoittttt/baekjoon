import sys
'''
실버2: 나무 자르기
필요한 크기 값을 구하는 방법: 
'''
input = sys.stdin.readline
N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

start, end = 1, max(tree)


while start <= end:
    midi = int((start + end) // 2)

    count = 0
    for i in tree:
        if i >= midi:
            count += i - midi

    if count >= M:
        start = midi + 1
    else:
        end = midi - 1

print(end)